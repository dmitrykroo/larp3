from src.models.data_models import User
from connectors.database_connector import DatabaseConnector
from utils.logger import setup_logger
from utils.data_validator import DataValidator
import uuid
import datetime

class UserService:
    """
    Service responsible for user management and operations.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.db_connector = DatabaseConnector(config['database'])
        self.validator = DataValidator(config.get('validation', {}))
        self.logger.info("UserService initialized.")

    def create_user(self, user_data):
        """
        Create a new user.

        Args:
            user_data (dict): Data for the new user.

        Returns:
            User: The created user object.
        """
        self.logger.info(f"Creating new user with data: {user_data}")
        if not self.validator.validate_user_creation(user_data):
            self.logger.error("User data validation failed.")
            raise ValueError("Invalid user data.")

        user_id = str(uuid.uuid4())
        new_user = User(
            id=user_id,
            username=user_data['username'],
            email=user_data['email'],
            registered_at=datetime.datetime.utcnow().isoformat(),
            nfts_owned=[]
        )
        self.db_connector.insert_user(new_user)
        self.logger.info(f"User created with ID: {user_id}")
        return new_user

    def get_user(self, user_id):
        """
        Retrieve user details by user ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            User: The user object.
        """
        self.logger.info(f"Retrieving user with ID: {user_id}")
        user_record = self.db_connector.fetch_user(user_id)
        if not user_record:
            self.logger.error(f"User with ID {user_id} not found.")
            raise ValueError("User not found.")
        user = User(**user_record)
        self.logger.debug(f"User retrieved: {user}")
        return user

    def update_user_nfts(self, user_id, nft_id):
        """
        Update the list of NFTs owned by the user.

        Args:
            user_id (str): The ID of the user.
            nft_id (str): The ID of the NFT to add.
        """
        self.logger.info(f"Updating NFTs for User ID: {user_id} with NFT ID: {nft_id}")
        user = self.get_user(user_id)
        if nft_id not in user.nfts_owned:
            user.nfts_owned.append(nft_id)
            self.db_connector.update_user_nfts(user_id, user.nfts_owned)
            self.logger.info(f"NFT ID {nft_id} added to User ID {user_id}.")
        else:
            self.logger.warning(f"NFT ID {nft_id} already exists for User ID {user_id}.")

    def delete_user(self, user_id):
        """
        Delete a user by user ID.

        Args:
            user_id (str): The ID of the user.
        """
        self.logger.info(f"Deleting user with ID: {user_id}")
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
