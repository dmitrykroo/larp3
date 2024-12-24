import unittest
from unittest.mock import MagicMock, patch
from src.connectors.api_connector import APIConnector

class TestAPIConnector(unittest.TestCase):
    def setUp(self):
        config = {
            'logging': {
                'name': 'test_logger',
                'level': 'DEBUG'
            },
            'base_url': 'https://api.test.com',
            'api_key': 'test_api_key',
            'timeout': 5
        }
        self.api_connector = APIConnector(config)

    @patch('requests.get')
    def test_get_market_trends_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'trend': 'up'}
        mock_get.return_value = mock_response

        result = self.api_connector.get_market_trends('test_collection')
        self.assertEqual(result, {'trend': 'up'})
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_market_trends_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        result = self.api_connector.get_market_trends('test_collection')
        self.assertEqual(result, {})
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_sentiment_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'sentiment': 'positive'}
        mock_get.return_value = mock_response

        result = self.api_connector.get_sentiment('nft123')
        self.assertEqual(result, 'positive')
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_sentiment_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = self.api_connector.get_sentiment('nft123')
        self.assertEqual(result, 'neutral')
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_collections_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'collections': ['Art', 'Music']}
        mock_get.return_value = mock_response

        result = self.api_connector.get_collections()
        self.assertEqual(result, ['Art', 'Music'])
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_collections_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        result = self.api_connector.get_collections()
        self.assertEqual(result, [])
        mock_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
