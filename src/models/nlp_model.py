import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import os
from utils.logger import setup_logger

class NLPModel:
    """
    Natural Language Processing model for sentiment analysis of NFT descriptions and related texts.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        nltk.download('vader_lexicon')
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.model_config = config.get('nlp', {})
        self.logger.info("NLP Model initialized.")

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the given text.

        Args:
            text (str): The text to analyze.

        Returns:
            dict: A dictionary containing sentiment scores.
        """
        self.logger.debug(f"Analyzing sentiment for text: {text}")
        sentiment_scores = self.sentiment_analyzer.polarity_scores(text)
        self.logger.debug(f"Sentiment scores: {sentiment_scores}")
        return sentiment_scores

    def load_custom_lexicon(self, lexicon_path):
        """
        Load a custom lexicon to enhance sentiment analysis.

        Args:
            lexicon_path (str): Path to the custom lexicon JSON file.
        """
        if os.path.exists(lexicon_path):
            self.logger.info(f"Loading custom lexicon from {lexicon_path}")
            with open(lexicon_path, 'r') as file:
                custom_lexicon = json.load(file)
            for word, score in custom_lexicon.items():
                self.sentiment_analyzer.lexicon[word] = score
            self.logger.info("Custom lexicon loaded successfully.")
        else:
            self.logger.warning(f"Custom lexicon file not found at {lexicon_path}")

    def preprocess_text(self, text):
        """
        Preprocess the input text for sentiment analysis.

        Args:
            text (str): The text to preprocess.

        Returns:
            str: The preprocessed text.
        """
        self.logger.debug(f"Preprocessing text: {text}")
        # Example preprocessing steps
        text = text.lower()
        text = ''.join([char for char in text if char.isalnum() or char.isspace()])
        self.logger.debug(f"Preprocessed text: {text}")
        return text

    def batch_analyze_sentiment(self, texts):
        """
        Analyze sentiment for a batch of texts.

        Args:
            texts (list of str): List of texts to analyze.

        Returns:
            list of dict: List of sentiment scores for each text.
        """
        self.logger.info(f"Starting batch sentiment analysis for {len(texts)} texts.")
        results = []
        for text in texts:
            preprocessed = self.preprocess_text(text)
            scores = self.analyze_sentiment(preprocessed)
            results.append(scores)
        self.logger.info("Batch sentiment analysis completed.")
        return results

    def save_sentiment_results(self, results, output_path):
        """
        Save sentiment analysis results to a JSON file.

        Args:
            results (list of dict): Sentiment analysis results.
            output_path (str): Path to save the results.
        """
        self.logger.info(f"Saving sentiment analysis results to {output_path}")
        with open(output_path, 'w') as file:
            json.dump(results, file, indent=4)
        self.logger.info("Sentiment analysis results saved successfully.")
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
