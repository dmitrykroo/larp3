from jsonschema import validate, ValidationError
from utils.logger import setup_logger

class DataValidator:
    """
    Utility class for validating data against predefined schemas.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.schemas = self._load_schemas(config.get('schemas_path', 'configs/schemas/'))
        self.logger.info("DataValidator initialized.")

    def _load_schemas(self, schemas_path):
        """
        Load JSON schemas from the specified directory.

        Args:
            schemas_path (str): Path to the schemas directory.

        Returns:
            dict: Dictionary of schemas.
        """
        import os
        import json
        self.logger.info(f"Loading schemas from {schemas_path}")
        schemas = {}
        for filename in os.listdir(schemas_path):
            if filename.endswith('.json'):
                schema_name = filename.replace('.json', '')
                with open(os.path.join(schemas_path, filename), 'r') as file:
                    schemas[schema_name] = json.load(file)
                self.logger.debug(f"Loaded schema: {schema_name}")
        return schemas

    def validate_nft(self, nft_data):
        """
        Validate NFT data against the NFT schema.

        Args:
            nft_data (dict): NFT data to validate.

        Returns:
            bool: Validation result.
        """
        self.logger.debug("Validating NFT data.")
        schema = self.schemas.get('nft')
        return self._validate(nft_data, schema)

    def validate_user(self, user_data):
        """
        Validate user data against the User schema.

        Args:
            user_data (dict): User data to validate.

        Returns:
            bool: Validation result.
        """
        self.logger.debug("Validating user data.")
        schema = self.schemas.get('user')
        return self._validate(user_data, schema)

    def validate_user_creation(self, user_data):
        """
        Validate user creation data against the UserCreation schema.

        Args:
            user_data (dict): User creation data to validate.

        Returns:
            bool: Validation result.
        """
        self.logger.debug("Validating user creation data.")
        schema = self.schemas.get('user_creation')
        return self._validate(user_data, schema)

    def validate_rarity(self, rarity_data):
        """
        Validate rarity data against the Rarity schema.

        Args:
            rarity_data (dict): Rarity data to validate.

        Returns:
            bool: Validation result.
        """
        self.logger.debug("Validating rarity data.")
        schema = self.schemas.get('rarity')
        return self._validate(rarity_data, schema)

    def _validate(self, data, schema):
        """
        Validate data against a given schema.

        Args:
            data (dict): Data to validate.
            schema (dict): JSON schema.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            validate(instance=data, schema=schema)
            self.logger.debug("Data validation successful.")
            return True
        except ValidationError as e:
            self.logger.error(f"Data validation error: {e.message}")
            return False
                                                              
                                                              
                                                              
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
