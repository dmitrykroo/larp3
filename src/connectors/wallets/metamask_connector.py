from web3 import Web3
from utils.logger import setup_logger

class MetaMaskConnector:
    """
    Connector to interact with MetaMask wallets.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.rpc_url = config.get('rpc_url')
        self.web3 = Web3(Web3.HTTPProvider(self.rpc_url))
        if self.web3.isConnected():
            self.logger.info("Connected to MetaMask wallet successfully.")
        else:
            self.logger.error("Failed to connect to MetaMask wallet.")
            raise ConnectionError("Cannot connect to MetaMask wallet.")

    def get_balance(self, wallet_address):
        """
        Get the Ether balance of a wallet.

        Args:
            wallet_address (str): The wallet address.

        Returns:
            float: Balance in Ether.
        """
        self.logger.debug(f"Fetching balance for wallet address: {wallet_address}")
        try:
            balance_wei = self.web3.eth.get_balance(wallet_address)
            balance_eth = self.web3.fromWei(balance_wei, 'ether')
            self.logger.debug(f"Balance for {wallet_address}: {balance_eth} ETH")
            return balance_eth
        except Exception as e:
            self.logger.error(f"Error fetching balance: {e}")
            return 0.0

    def send_transaction(self, private_key, to_address, value):
        """
        Send Ether from the connected wallet to another address.

        Args:
            private_key (str): Private key of the sender.
            to_address (str): Recipient wallet address.
            value (float): Amount of Ether to send.

        Returns:
            str: Transaction hash.
        """
        self.logger.info(f"Sending {value} ETH from {self.web3.eth.account.privateKeyToAccount(private_key).address} to {to_address}")
        try:
            account = self.web3.eth.account.privateKeyToAccount(private_key)
            nonce = self.web3.eth.get_transaction_count(account.address)
            tx = {
                'nonce': nonce,
                'to': to_address,
                'value': self.web3.toWei(value, 'ether'),
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei')
            }
            signed_tx = account.sign_transaction(tx)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            self.logger.info(f"Transaction sent with hash: {tx_hash.hex()}")
            return tx_hash.hex()
        except Exception as e:
            self.logger.error(f"Failed to send transaction: {e}")
            return ""