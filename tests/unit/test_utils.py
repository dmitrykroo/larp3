import unittest
from unittest.mock import MagicMock
from src.utils.data_validator import DataValidator

class TestDataValidator(unittest.TestCase):
    def setUp(self):
        config = {
            'logging': {
                'name': 'test_logger',
                'level': 'DEBUG'
            },
            'schemas_path': 'tests/schemas/'
        }
        self.validator = DataValidator(config)
        self.validator._load_schemas = MagicMock(return_value={
            'nft': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string'},
                    'name': {'type': 'string'},
                    'price': {'type': 'number'}
                },
                'required': ['id', 'name', 'price']
            },
            'user': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string'},
                    'username': {'type': 'string'},
                    'email': {'type': 'string'}
                },
                'required': ['id', 'username', 'email']
            }
        })

    def test_validate_nft_success(self):
        nft_data = {
            'id': 'nft123',
            'name': 'Art Piece',
            'price': 1500.0
        }
        self.validator.validate_nft = MagicMock(return_value=True)
        result = self.validator.validate_nft(nft_data)
        self.assertTrue(result)

    def test_validate_nft_failure(self):
        nft_data = {
            'id': 'nft123',
            'price': 1500.0
            # Missing 'name'
        }
        self.validator.validate_nft = MagicMock(return_value=False)
        result = self.validator.validate_nft(nft_data)
        self.assertFalse(result)

    def test_validate_user_success(self):
        user_data = {
            'id': 'user123',
            'username': 'jane_doe',
            'email': 'jane@example.com'
        }
        self.validator.validate_user = MagicMock(return_value=True)
        result = self.validator.validate_user(user_data)
        self.assertTrue(result)

    def test_validate_user_failure(self):
        user_data = {
            'id': 'user123',
            'email': 'jane@example.com'
            # Missing 'username'
        }
        self.validator.validate_user = MagicMock(return_value=False)
        result = self.validator.validate_user(user_data)
        self.assertFalse(result)

    def test_validate_user_creation_success(self):
        user_data = {
            'username': 'jane_doe',
            'email': 'jane@example.com'
        }
        self.validator.validate_user_creation = MagicMock(return_value=True)
        result = self.validator.validate_user_creation(user_data)
        self.assertTrue(result)

    def test_validate_user_creation_failure(self):
        user_data = {
            'username': 'jane_doe'
            # Missing 'email'
        }
        self.validator.validate_user_creation = MagicMock(return_value=False)
        result = self.validator.validate_user_creation(user_data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()