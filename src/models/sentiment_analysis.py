from src.models.nlp_model import NLPModel
from utils.config_loader import ConfigLoader
from utils.logger import setup_logger

class SentimentAnalysis:
    """
    Class to handle sentiment analysis for NFT-related texts.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.nlp_model = NLPModel(config)
        lexicon_path = config.get('nlp', {}).get('custom_lexicon_path', 'data/lexicons/custom_lexicon.json')
        self.nlp_model.load_custom_lexicon(lexicon_path)
        self.logger.info("SentimentAnalysis initialized.")

    def analyze_text(self, text):
        """
        Analyze the sentiment of a single text input.

        Args:
            text (str): The text to analyze.

        Returns:
            dict: Sentiment scores.
        """
        self.logger.debug(f"Analyzing sentiment for text: {text}")
        return self.nlp_model.analyze_sentiment(text)

    def analyze_texts_batch(self, texts):
        """
        Analyze sentiment for a batch of texts.

        Args:
            texts (list of str): List of texts to analyze.

        Returns:
            list of dict: List of sentiment scores.
        """
        self.logger.debug(f"Analyzing sentiment for a batch of {len(texts)} texts.")
        return self.nlp_model.batch_analyze_sentiment(texts)