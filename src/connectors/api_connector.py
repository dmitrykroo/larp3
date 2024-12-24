import requests
from utils.logger import setup_logger

class APIConnector:
    """
    Connector to interact with external APIs for data retrieval.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.base_url = config.get('base_url')
        self.api_key = config.get('api_key')
        self.timeout = config.get('timeout', 10)
        self.logger.info("APIConnector initialized.")

    def get_market_trends(self, collection):
        """
        Retrieve market trends for a specific NFT collection.

        Args:
            collection (str): The name of the NFT collection.

        Returns:
            dict: Market trends data.
        """
        endpoint = f"{self.base_url}/market_trends/{collection}"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        self.logger.debug(f"Fetching market trends from {endpoint}")
        try:
            response = requests.get(endpoint, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            self.logger.debug("Market trends data retrieved successfully.")
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch market trends: {e}")
            return {}

    def get_sentiment(self, nft_id):
        """
        Retrieve sentiment analysis for a specific NFT.

        Args:
            nft_id (str): The ID of the NFT.

        Returns:
            str: Sentiment value ('positive', 'neutral', 'negative').
        """
        endpoint = f"{self.base_url}/sentiment/{nft_id}"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        self.logger.debug(f"Fetching sentiment from {endpoint}")
        try:
            response = requests.get(endpoint, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            sentiment = response.json().get('sentiment', 'neutral')
            self.logger.debug(f"Sentiment retrieved: {sentiment}")
            return sentiment
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch sentiment: {e}")
            return 'neutral'

    def get_collections(self):
        """
        Retrieve a list of all NFT collections.

        Returns:
            list of str: List of collection names.
        """
        endpoint = f"{self.base_url}/collections"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        self.logger.debug(f"Fetching collections from {endpoint}")
        try:
            response = requests.get(endpoint, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            collections = response.json().get('collections', [])
            self.logger.debug(f"Collections retrieved: {collections}")
            return collections
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch collections: {e}")
            return []
            
            
            
            
            
            
            
            
            
            
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
