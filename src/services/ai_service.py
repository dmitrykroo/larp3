from src.llm.gpt_integration import GPTIntegration
from src.models.sentiment_analysis import SentimentAnalysis
from src.models.pricing_model import PricingModel
from utils.logger import setup_logger

class AIService:
    """
    Service responsible for AI-driven functionalities such as report generation and insights.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.sentiment_analysis = SentimentAnalysis(config)
        self.pricing_model = PricingModel(config['model'])
        self.gpt_integration = GPTIntegration(config['llm'])
        self.logger.info("AIService initialized.")

    def generate_insights(self, nft_data, market_data):
        """
        Generate insights based on NFT data and market trends.

        Args:
            nft_data (dict): Processed NFT data.
            market_data (dict): Aggregated market data.

        Returns:
            str: Generated insights.
        """
        self.logger.info(f"Generating insights for NFT ID: {nft_data.get('id')}")
        sentiment_scores = self.sentiment_analysis.analyze_text(nft_data.get('description', ''))
        price_prediction = self.pricing_model.predict({
            'rarity': self._encode_rarity(nft_data.get('rarity', 'common')),
            'num_historical_prices': len(nft_data.get('historical_prices', [])),
            'market_trend': market_data.get('average_price', 0),
            'sentiment': 1 if sentiment_scores.get('compound', 0) > 0 else -1
        })
        insights = f"The NFT '{nft_data.get('name')}' has a sentiment score of {sentiment_scores.get('compound', 0)} and a predicted price of ${price_prediction:.2f}."
        self.logger.debug(f"Generated insights: {insights}")
        return insights

    def generate_report(self, user_id, nft_list, market_data):
        """
        Generate a comprehensive report for a user based on their NFTs and market data.

        Args:
            user_id (str): The ID of the user.
            nft_list (list of dict): List of user's NFTs.
            market_data (dict): Aggregated market data.

        Returns:
            str: Generated report text.
        """
        self.logger.info(f"Generating report for User ID: {user_id}")
        report_sections = []
        for nft in nft_list:
            insights = self.generate_insights(nft, market_data)
            report_sections.append(insights)
        report_text = self.gpt_integration.generate_report_text({
            'user_id': user_id,
            'valuations': report_sections
        })
        self.logger.debug("Report generation completed.")
        return report_text

    def _encode_rarity(self, rarity):
        """
        Encode rarity into a numerical value for model prediction.

        Args:
            rarity (str): Rarity level.

        Returns:
            int: Encoded rarity.
        """
        rarity_mapping = {
            'common': 1,
            'uncommon': 2,
            'rare': 3,
            'epic': 4,
            'legendary': 5
        }
        encoded = rarity_mapping.get(rarity.lower(), 1)
        self.logger.debug(f"Encoded rarity '{rarity}' to {encoded}")
        return encoded
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
