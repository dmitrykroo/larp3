import openai
from utils.logger import setup_logger

class GPTIntegration:
    """
    Integration with GPT-based language models for report generation.
    """

    def __init__(self, config):
        self.api_key = config['api_key']
        self.model = config['model']
        self.temperature = config.get('temperature', 0.7)
        openai.api_key = self.api_key
        self.logger = setup_logger(config.get('logging', {}))

    def generate_report_text(self, report_data):
        prompt = self._build_prompt(report_data)
        self.logger.debug(f"Generated prompt for GPT: {prompt}")
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a professional NFT Valuation Advisor."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=500
            )
            report_text = response['choices'][0]['message']['content'].strip()
            self.logger.debug(f"GPT response: {report_text}")
            return report_text
        except Exception as e:
            self.logger.error(f"Error generating report with GPT: {e}")
            raise

    def _build_prompt(self, report_data):
        prompt = f"Generate a comprehensive NFT valuation report for user {report_data['user_id']}.\n"
        prompt += f"Report generated at: {report_data['generated_at']}\n"
        prompt += "Valuations:\n"
        for valuation in report_data['valuations']:
            prompt += f"- NFT ID: {valuation['nft_id']}, Valuation: ${valuation['valuation']}, Date: {valuation['timestamp']}\n"
        prompt += "\nProvide insights and recommendations based on the valuations."
        return prompt
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
