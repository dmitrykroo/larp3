import requests
from utils.logger import setup_logger

class RarityAPI:
    """
    Connector to interact with the Rarity API.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.api_url = config.get('api_url')
        self.api_key = config.get('api_key')
        self.timeout = config.get('timeout', 10)
        self.logger.info("RarityAPI connector initialized.")

    def get_rarity(self, nft_id):
        """
        Retrieve rarity information for a specific NFT.

        Args:
            nft_id (str): The ID of the NFT.

        Returns:
            dict: Rarity details.
        """
        endpoint = f"{self.api_url}/rarity/{nft_id}"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        self.logger.debug(f"Fetching rarity data from {endpoint}")
        try:
            response = requests.get(endpoint, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            rarity_data = response.json().get('rarity', {})
            self.logger.debug(f"Rarity data retrieved: {rarity_data}")
            return rarity_data
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch rarity data: {e}")
            return {}