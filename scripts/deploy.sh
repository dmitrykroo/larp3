import requests
from utils.logger import setup_logger

class EtherscanAPI:
    """
    Connector to interact with the Etherscan API.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.api_url = config.get('api_url')
        self.api_key = config.get('api_key')
        self.timeout = config.get('timeout', 10)
        self.logger.info("EtherscanAPI connector initialized.")

    def get_transaction_history(self, wallet_address):
        """
        Retrieve transaction history for a specific wallet address.

        Args:
            wallet_address (str): The Ethereum wallet address.

        Returns:
            list of dict: List of transactions.
        """
        endpoint = f"{self.api_url}/api"
        params = {
            'module': 'account',
            'action': 'txlist',
            'address': wallet_address,
            'startblock': 0,
            'endblock': 99999999,
            'sort': 'asc',
            'apikey': self.api_key
        }
        self.logger.debug(f"Fetching transaction history from {endpoint} for address {wallet_address}")
        try:
            response = requests.get(endpoint, params=params, timeout=self.timeout)
            response.raise_for_status()
            transactions = response.json().get('result', [])
            self.logger.debug(f"Retrieved {len(transactions)} transactions from Etherscan.")
            return transactions
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch transaction history: {e}")
            return []