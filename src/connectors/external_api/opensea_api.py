import requests
from utils.logger import setup_logger

class OpenSeaAPI:
    """
    Connector to interact with the OpenSea API.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.api_url = config.get('api_url')
        self.api_key = config.get('api_key')
        self.timeout = config.get('timeout', 10)
        self.logger.info("OpenSeaAPI connector initialized.")

    def get_market_data(self, collection):
        """
        Retrieve market data for a specific collection from OpenSea.

        Args:
            collection (str): The name of the NFT collection.

        Returns:
            list of dict: Market data entries.
        """
        endpoint = f"{self.api_url}/assets"
        params = {
            'collection': collection,
            'order_direction': 'desc',
            'offset': 0,
            'limit': 50
        }
        headers = {'X-API-KEY': self.api_key}
        self.logger.debug(f"Fetching market data from {endpoint} with params {params}")
        try:
            response = requests.get(endpoint, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            assets = response.json().get('assets', [])
            self.logger.debug(f"Retrieved {len(assets)} assets from OpenSea.")
            return assets
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch market data from OpenSea: {e}")
            return []

    def get_collection_stats(self, collection):
        """
        Retrieve statistics for a specific collection.

        Args:
            collection (str): The name of the NFT collection.

        Returns:
            dict: Collection statistics.
        """
        endpoint = f"{self.api_url}/collection/{collection}/stats"
        headers = {'X-API-KEY': self.api_key}
        self.logger.debug(f"Fetching collection stats from {endpoint}")
        try:
            response = requests.get(endpoint, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            stats = response.json().get('stats', {})
            self.logger.debug(f"Collection stats retrieved: {stats}")
            return stats
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch collection stats from OpenSea: {e}")
            return {}