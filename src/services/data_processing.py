import pandas as pd
import numpy as np
from utils.logger import setup_logger
from utils.cache import Cache

class DataProcessing:
    """
    Service responsible for processing and transforming ingested data.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.cache = Cache(config.get('cache', {}))
        self.processing_config = config.get('processing', {})
        self.logger.info("DataProcessing service initialized.")

    def clean_market_data(self, df):
        """
        Clean and preprocess market data.

        Args:
            df (pd.DataFrame): Raw market data.

        Returns:
            pd.DataFrame: Cleaned market data.
        """
        self.logger.info("Starting market data cleaning.")
        initial_count = len(df)
        df.dropna(inplace=True)
        df = df[df['price'] > 0]
        df['date'] = pd.to_datetime(df['date'])
        df.sort_values('date', inplace=True)
        final_count = len(df)
        self.logger.info(f"Market data cleaned. Rows before: {initial_count}, after: {final_count}")
        return df

    def enrich_market_data(self, df):
        """
        Enrich market data with additional features.

        Args:
            df (pd.DataFrame): Cleaned market data.

        Returns:
            pd.DataFrame: Enriched market data.
        """
        self.logger.info("Starting market data enrichment.")
        df['price_change'] = df['price'].pct_change().fillna(0)
        df['rolling_avg_7'] = df['price'].rolling(window=7).mean().fillna(method='bfill')
        df['rolling_std_7'] = df['price'].rolling(window=7).std().fillna(0)
        self.logger.info("Market data enrichment completed.")
        return df

    def aggregate_market_data(self, df):
        """
        Aggregate market data to generate summary statistics.

        Args:
            df (pd.DataFrame): Enriched market data.

        Returns:
            dict: Aggregated market data statistics.
        """
        self.logger.info("Aggregating market data.")
        aggregation = {
            'average_price': df['price'].mean(),
            'median_price': df['price'].median(),
            'max_price': df['price'].max(),
            'min_price': df['price'].min(),
            'std_dev_price': df['price'].std(),
            'total_volume': df['volume'].sum()
        }
        self.logger.debug(f"Aggregated market data: {aggregation}")
        return aggregation

    def process_nft_data(self, nft_data):
        """
        Process individual NFT data.

        Args:
            nft_data (dict): Raw NFT data.

        Returns:
            dict: Processed NFT data.
        """
        self.logger.info(f"Processing data for NFT ID: {nft_data.get('id')}")
        # Example processing steps
        nft_data['normalized_price'] = self._normalize_price(nft_data.get('price', 0))
        nft_data['price_trend'] = self._determine_trend(nft_data.get('historical_prices', []))
        self.logger.debug(f"Processed NFT data: {nft_data}")
        return nft_data

    def _normalize_price(self, price):
        """
        Normalize the price based on predefined scaling.

        Args:
            price (float): The price to normalize.

        Returns:
            float: Normalized price.
        """
        self.logger.debug(f"Normalizing price: {price}")
        normalized = price / 1000  # Example normalization
        self.logger.debug(f"Normalized price: {normalized}")
        return normalized

    def _determine_trend(self, historical_prices):
        """
        Determine the price trend based on historical prices.

        Args:
            historical_prices (list of float): Historical price data.

        Returns:
            str: 'up', 'down', or 'stable' trend.
        """
        self.logger.debug(f"Determining trend for historical prices: {historical_prices}")
        if len(historical_prices) < 2:
            return 'stable'
        trend = 'up' if historical_prices[-1] > historical_prices[0] else 'down'
        self.logger.debug(f"Determined trend: {trend}")
        return trend

    def cache_aggregated_data(self, key, data):
        """
        Cache aggregated data.

        Args:
            key (str): Cache key.
            data (dict): Data to cache.
        """
        self.logger.info(f"Caching aggregated data with key: {key}")
        self.cache.set(key, data, ttl=self.processing_config.get('cache_ttl', 3600))
        self.logger.info("Aggregated data cached successfully.")

    def get_cached_aggregated_data(self, key):
        """
        Retrieve cached aggregated data.

        Args:
            key (str): Cache key.

        Returns:
            dict or None: Cached data or None if not found.
        """
        self.logger.info(f"Retrieving cached aggregated data with key: {key}")
        return self.cache.get(key)