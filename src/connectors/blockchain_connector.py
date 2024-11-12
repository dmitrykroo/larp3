import requests
from utils.logger import setup_logger

class BlockchainConnector:
    """
    Connector to interact with the blockchain for NFT data.
    """

    def __init__(self, config):
        self.api_url = config['api_url']
        self.api_key = config['api_key']
        self.logger = setup_logger(config['logging'])

    def get_nft_details(self, nft_id):
        self.logger.debug(f"Fetching NFT details from blockchain for ID: {nft_id}")
        response = requests.get(f"{self.api_url}/nfts/{nft_id}", headers={'Authorization': f"Bearer {self.api_key}"})
        if response.status_code == 200:
            self.logger.debug(f"NFT details retrieved: {response.json()}")
            return response.json()
        self.logger.error(f"Failed to fetch NFT details: {response.status_code}")
        return None

    def add_nft(self, data):
        self.logger.debug("Adding new NFT to blockchain")
        response = requests.post(f"{self.api_url}/nfts", json=data, headers={'Authorization': f"Bearer {self.api_key}"})
        if response.status_code == 201:
            self.logger.debug(f"NFT added successfully: {response.json()}")
            return response.json()
        self.logger.error(f"Failed to add NFT: {response.status_code}")
        raise Exception("Failed to add NFT to blockchain")

    def get_user_nfts(self, user_id):
        self.logger.debug(f"Fetching NFTs for User ID: {user_id}")
        response = requests.get(f"{self.api_url}/users/{user_id}/nfts", headers={'Authorization': f"Bearer {self.api_key}"})
        if response.status_code == 200:
            self.logger.debug(f"User NFTs retrieved: {response.json()}")
            return response.json()
        self.logger.error(f"Failed to fetch user NFTs: {response.status_code}")
        return []
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
