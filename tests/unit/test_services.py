import unittest
from unittest.mock import MagicMock
from src.services.user_service import UserService
from src.models.data_models import User

class TestUserService(unittest.TestCase):
    def setUp(self):
        config = {
            'logging': {
                'name': 'test_logger',
                'level': 'DEBUG'
            },
            'database': {
                'host': 'localhost',
                'port': 5432,
                'username': 'test_user',
                'password': 'test_pass',
                'dbname': 'test_db'
            },
            'validation': {
                'schemas_path': 'configs/schemas/'
            }
        }
        self.user_service = UserService(config)
        self.user_service.db_connector = MagicMock()
        self.user_service.validator = MagicMock()
        self.user_service.validator.validate_user_creation.return_value = True
        self.user_service.validator.validate_user.return_value = True

    def test_create_user_success(self):
        user_data = {
            'username': 'jane_doe',
            'email': 'jane@example.com'
        }
        self.user_service.db_connector.insert_user = MagicMock()
        user = self.user_service.create_user(user_data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'jane_doe')
        self.assertEqual(user.email, 'jane@example.com')
        self.user_service.db_connector.insert_user.assert_called_once()

    def test_create_user_validation_failure(self):
        user_data = {
            'username': 'jane_doe'
            # Missing email
        }
        self.user_service.validator.validate_user_creation.return_value = False
        with self.assertRaises(ValueError):
            self.user_service.create_user(user_data)

    def test_get_user_success(self):
        user_id = 'user123'
        user_record = {
            'id': 'user123',
            'username': 'jane_doe',
            'email': 'jane@example.com',
            'registered_at': '2025-01-01T12:00:00Z',
            'nfts_owned': ['nft123']
        }
        self.user_service.db_connector.fetch_user.return_value = user_record
        user = self.user_service.get_user(user_id)
        self.assertEqual(user.id, 'user123')
        self.assertEqual(user.username, 'jane_doe')
        self.user_service.db_connector.fetch_user.assert_called_with(user_id)

    def test_get_user_not_found(self):
        user_id = 'user123'
        self.user_service.db_connector.fetch_user.return_value = None
        with self.assertRaises(ValueError):
            self.user_service.get_user(user_id)

    def test_update_user_nfts(self):
        user_id = 'user123'
        nft_id = 'nft456'
        user = User(
            id=user_id,
            username='jane_doe',
            email='jane@example.com',
            registered_at='2025-01-01T12:00:00Z',
            nfts_owned=['nft123']
        )
        self.user_service.get_user = MagicMock(return_value=user)
        self.user_service.db_connector.update_user_nfts = MagicMock()
        self.user_service.update_user_nfts(user_id, nft_id)
        self.assertIn(nft_id, user.nfts_owned)
        self.user_service.db_connector.update_user_nfts.assert_called_with(user_id, user.nfts_owned)

    def test_delete_user(self):
        user_id = 'user123'
        self.user_service.db_connector.delete_user = MagicMock()
        self.user_service.delete_user(user_id)
        self.user_service.db_connector.delete_user.assert_called_with(user_id)

if __name__ == '__main__':
    unittest.main()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
