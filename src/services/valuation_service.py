import datetime
from connectors.blockchain_connector import BlockchainConnector
from connectors.api_connector import APIConnector
from models.valuation_model import ValuationModel
from utils.logger import setup_logger
from utils.cache import Cache
from llm.gpt_integration import GPTIntegration

class ValuationService:
    """
    Service responsible for NFT valuation logic.
    """

    def __init__(self, config):
        self.config = config
        self.blockchain = BlockchainConnector(config['blockchain'])
        self.api = APIConnector(config['api'])
        self.model = ValuationModel(config['model'])
        self.logger = setup_logger(config['logging'])
        self.cache = Cache(config['cache'])
        self.llm = GPTIntegration(config['llm'])

    def get_nft_details(self, nft_id):
        self.logger.debug(f"Fetching details for NFT ID: {nft_id}")
        details = self.blockchain.get_nft_details(nft_id)
        if not details:
            self.logger.error(f"No details found for NFT ID: {nft_id}")
            raise ValueError("NFT details not found")
        self.logger.debug(f"Details retrieved: {details}")
        return details

    def calculate_valuation(self, nft, user):
        self.logger.info(f"Calculating valuation for NFT ID: {nft['id']} for User ID: {user['id']}")
        market_trends = self.api.get_market_trends(nft['collection'])
        sentiment = self.api.get_sentiment(nft['id'])
        self.logger.debug(f"Market Trends: {market_trends}, Sentiment: {sentiment}")
        
        cached_val = self.cache.get(nft['id'])
        if cached_val:
            self.logger.info(f"Using cached valuation for NFT ID: {nft['id']}")
            return cached_val
        
        features = {
            'rarity': nft['rarity'],
            'historical_prices': nft['historical_prices'],
            'market_trends': market_trends,
            'sentiment': sentiment
        }
        valuation = self.model.predict(features)
        self.cache.set(nft['id'], valuation, ttl=3600)
        self.logger.info(f"Valuation for NFT ID: {nft['id']} is {valuation}")
        return valuation

    def add_nft(self, data):
        self.logger.info("Adding new NFT")
        nft = self.blockchain.add_nft(data)
        self.logger.debug(f"NFT added: {nft}")
        return nft

    def get_latest_valuation(self, nft_id):
        self.logger.info(f"Retrieving latest valuation for NFT ID: {nft_id}")
        valuation = self.cache.get(nft_id)
        if valuation:
            self.logger.debug(f"Valuation retrieved from cache: {valuation}")
            return valuation
        valuation = self.model.get_latest(nft_id)
        if valuation:
            self.cache.set(nft_id, valuation, ttl=3600)
        self.logger.debug(f"Valuation retrieved from model: {valuation}")
        return valuation

    def generate_user_report(self, user_id):
        self.logger.info(f"Generating report for User ID: {user_id}")
        user_nfts = self.blockchain.get_user_nfts(user_id)
        valuations = []
        for nft in user_nfts:
            valuation = self.calculate_valuation(nft, {'id': user_id})
            valuations.append({
                'nft_id': nft['id'],
                'valuation': valuation,
                'timestamp': datetime.datetime.utcnow().isoformat()
            })
        report = {
            'user_id': user_id,
            'generated_at': datetime.datetime.utcnow().isoformat(),















