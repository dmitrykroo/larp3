import unittest
from unittest.mock import MagicMock, patch
from src.llm.gpt_integration import GPTIntegration

class TestGPTIntegration(unittest.TestCase):
    def setUp(self):
        config = {
            'logging': {
                'name': 'test_logger',
                'level': 'DEBUG'
            },
            'api_key': 'test_openai_api_key',
            'model': 'gpt-4',
            'temperature': 0.7
        }
        self.gpt = GPTIntegration(config)

    @patch('openai.ChatCompletion.create')
    def test_generate_report_text_success(self, mock_create):
        mock_response = {
            'choices': [{
                'message': {
                    'content': 'Generated report content.'
                }
            }]
        }
        mock_create.return_value = mock_response

        report_data = {
            'user_id': 'user123',
            'generated_at': '2025-01-24T17:00:00Z',
            'valuations': [
                {'nft_id': 'nft123', 'valuation': 2500, 'timestamp': '2025-01-24T16:30:00Z'}
            ]
        }
        result = self.gpt.generate_report_text(report_data)
        self.assertEqual(result, 'Generated report content.')
        mock_create.assert_called_once()

    @patch('openai.ChatCompletion.create')
    def test_generate_report_text_failure(self, mock_create):
        mock_create.side_effect = Exception("OpenAI API error")

        report_data = {
            'user_id': 'user123',
            'generated_at': '2025-01-24T17:00:00Z',
            'valuations': []
        }
        with self.assertRaises(Exception):
            self.gpt.generate_report_text(report_data)
        mock_create.assert_called_once()

    def test_build_prompt(self):
        report_data = {
            'user_id': 'user123',
            'generated_at': '2025-01-24T17:00:00Z',
            'valuations': [
                {'nft_id': 'nft123', 'valuation': 2500, 'timestamp': '2025-01-24T16:30:00Z'}
            ]
        }
        prompt = self.gpt._build_prompt(report_data)
        expected_prompt = (
            "Generate a comprehensive NFT valuation report for user user123.\n"
            "Report generated at: 2025-01-24T17:00:00Z\n"
            "Valuations:\n"
            "- NFT ID: nft123, Valuation: $2500, Date: 2025-01-24T16:30:00Z\n\n"
            "Provide insights and recommendations based on the valuations."
        )
        self.assertEqual(prompt, expected_prompt)

if __name__ == '__main__':
    unittest.main()
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
