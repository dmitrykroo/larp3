import redis
from utils.logger import setup_logger

class Cache:
    """
    Utility class for caching data using Redis.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.host = config.get('host', 'localhost')
        self.port = config.get('port', 6379)
        self.db = config.get('db', 0)
        self.password = config.get('password', None)
        try:
            self.client = redis.Redis(host=self.host, port=self.port, db=self.db, password=self.password)
            self.client.ping()
            self.logger.info("Connected to Redis cache successfully.")
        except redis.ConnectionError as e:
            self.logger.error(f"Failed to connect to Redis: {e}")
            self.client = None

    def set(self, key, value, ttl=3600):
        """
        Set a value in the cache with a time-to-live.

        Args:
            key (str): Cache key.
            value (str): Value to cache.
            ttl (int): Time-to-live in seconds.
        """
        if not self.client:
            self.logger.error("Redis client is not available.")
            return
        try:
            self.client.setex(key, ttl, value)
            self.logger.debug(f"Cached key: {key} with TTL: {ttl}")
        except Exception as e:
            self.logger.error(f"Failed to set cache key {key}: {e}")

    def get(self, key):
        """
        Retrieve a value from the cache.

        Args:
            key (str): Cache key.

        Returns:
            str or None: Cached value or None if not found.
        """
        if not self.client:
            self.logger.error("Redis client is not available.")
            return None
        try:
            value = self.client.get(key)
            if value:
                self.logger.debug(f"Retrieved cache key: {key}")
                return value.decode('utf-8')
            else:
                self.logger.debug(f"Cache key {key} not found.")
                return None
        except Exception as e:
            self.logger.error(f"Failed to get cache key {key}: {e}")
            return None

    def delete(self, key):
        """
        Delete a key from the cache.

        Args:
            key (str): Cache key.
        """
        if not self.client:
            self.logger.error("Redis client is not available.")
            return
        try:
            self.client.delete(key)
            self.logger.debug(f"Deleted cache key: {key}")
        except Exception as e:
            self.logger.error(f"Failed to delete cache key {key}: {e}")

    def flush_all(self):
        """
        Flush all keys from the cache.
        """
        if not self.client:
            self.logger.error("Redis client is not available.")
            return
        try:
            self.client.flushall()
            self.logger.info("Flushed all cache keys.")
        except Exception as e:
            self.logger.error(f"Failed to flush cache: {e}")
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
