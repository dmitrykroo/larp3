import yaml
from utils.logger import setup_logger

class ConfigLoader:
    """
    Utility class for loading configuration files.
    """

    @staticmethod
    def load_config(config_path):
        """
        Load configuration from a YAML file.

        Args:
            config_path (str): Path to the YAML configuration file.

        Returns:
            dict: Configuration data.
        """
        logger = setup_logger({})
        logger.info(f"Loading configuration from {config_path}")
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
            logger.debug("Configuration loaded successfully.")
            return config
        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")
            return {}