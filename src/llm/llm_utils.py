import openai
from utils.logger import setup_logger

class LLMUtils:
    """
    Utility class for interacting with Large Language Models (LLMs).
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.api_key = config.get('api_key')
        self.model = config.get('model', 'gpt-4')
        self.temperature = config.get('temperature', 0.7)
        openai.api_key = self.api_key
        self.logger.info("LLMUtils initialized.")

    def generate_text(self, prompt, max_tokens=150):
        """
        Generate text using the LLM.

        Args:
            prompt (str): The input prompt.
            max_tokens (int): Maximum number of tokens to generate.

        Returns:
            str: Generated text.
        """
        self.logger.debug(f"Generating text with prompt: {prompt}")
        try:
            response = openai.Completion.create(
                engine=self.model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=self.temperature
            )
            generated_text = response.choices[0].text.strip()
            self.logger.debug(f"Generated text: {generated_text}")
            return generated_text
        except Exception as e:
            self.logger.error(f"Failed to generate text: {e}")
            return ""