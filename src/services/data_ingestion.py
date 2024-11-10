import pandas as pd
import json
from connectors.external_api.opensea_api import OpenSeaAPI
from connectors.external_api.rariry_api import RarityAPI
from connectors.blockchain_connector import BlockchainConnector
from utils.logger import setup_logger
from utils.data_validator import DataValidator

class DataIngestion:
    """
    Service responsible for ingesting data from various sources.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.blockchain = BlockchainConnector(config['blockchain'])
        self.opensea_api = OpenSeaAPI(config['external_api']['opensea'])
        self.rarity_api = RarityAPI(config['external_api']['rarity'])
        self.validator = DataValidator(config.get('validation', {}))
        self.logger.info("DataIngestion service initialized.")

    def ingest_blockchain_data(self, nft_id):
        """
        Ingest data for a specific NFT from the blockchain.

        Args:
            nft_id (str): The ID of the NFT.

        Returns:
            dict: NFT details.
        """
        self.logger.info(f"Ingesting blockchain data for NFT ID: {nft_id}")
        nft_details = self.blockchain.get_nft_details(nft_id)
        if nft_details and self.validator.validate_nft(nft_details):
            self.logger.debug(f"Blockchain data for NFT ID {nft_id} validated successfully.")
            return nft_details
        else:
            self.logger.error(f"Invalid or incomplete blockchain data for NFT ID: {nft_id}")
            return {}

    def ingest_market_data(self, collection):
        """
        Ingest market data for a specific NFT collection.

        Args:
            collection (str): The name of the NFT collection.

        Returns:
            pd.DataFrame: Market data.
        """
        self.logger.info(f"Ingesting market data for collection: {collection}")
        market_data = self.opensea_api.get_market_data(collection)
        if market_data is not None:
            df = pd.DataFrame(market_data)
            self.logger.debug(f"Market data for collection {collection} ingested successfully.")
            return df
        else:
            self.logger.error(f"Failed to ingest market data for collection: {collection}")
            return pd.DataFrame()

    def ingest_rarity_data(self, nft_id):
        """
        Ingest rarity data for a specific NFT.

        Args:
            nft_id (str): The ID of the NFT.

        Returns:
            dict: Rarity details.
        """
        self.logger.info(f"Ingesting rarity data for NFT ID: {nft_id}")
        rarity_data = self.rarity_api.get_rarity(nft_id)
        if rarity_data and self.validator.validate_rarity(rarity_data):
            self.logger.debug(f"Rarity data for NFT ID {nft_id} validated successfully.")
            return rarity_data
        else:
            self.logger.error(f"Invalid or incomplete rarity data for NFT ID: {nft_id}")
            return {}

    def ingest_user_data(self, user_id):
        """
        Ingest data for a specific user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: User details.
        """
        self.logger.info(f"Ingesting data for User ID: {user_id}")
        user_data = self.blockchain.get_user_details(user_id)
        if user_data and self.validator.validate_user(user_data):
            self.logger.debug(f"User data for User ID {user_id} validated successfully.")
            return user_data
        else:
            self.logger.error(f"Invalid or incomplete user data for User ID: {user_id}")
            return {}

    def ingest_all_data_for_nft(self, nft_id):
        """
        Ingest all relevant data for a specific NFT.

        Args:
            nft_id (str): The ID of the NFT.

        Returns:
            dict: Aggregated NFT data.
        """
        self.logger.info(f"Starting full data ingestion for NFT ID: {nft_id}")
        blockchain_data = self.ingest_blockchain_data(nft_id)
        rarity_data = self.ingest_rarity_data(nft_id)
        aggregated_data = {**blockchain_data, **rarity_data}
        self.logger.info(f"Data ingestion completed for NFT ID: {nft_id}")
        return aggregated_data

    def ingest_data_bulk(self, nft_ids):
        """
        Ingest data for multiple NFTs.

        Args:
            nft_ids (list of str): List of NFT IDs.

        Returns:
            list of dict: List of aggregated NFT data.
        """
        self.logger.info(f"Starting bulk data ingestion for {len(nft_ids)} NFTs.")
        aggregated_data_list = []
        for nft_id in nft_ids:
            data = self.ingest_all_data_for_nft(nft_id)
            if data:
                aggregated_data_list.append(data)
        self.logger.info("Bulk data ingestion completed.")
        return aggregated_data_list

    def ingest_market_trends(self):
        """
        Ingest and update market trends for all collections.

        Returns:
            dict: Market trends data.
        """
        self.logger.info("Ingesting market trends for all collections.")
        collections = self.opensea_api.get_collections()
        trends = {}
        for collection in collections:
            market_data = self.ingest_market_data(collection)
            if not market_data.empty:
                trends[collection] = market_data.describe().to_dict()
        self.logger.info("Market trends ingestion completed.")
        return trends