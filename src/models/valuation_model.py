from sklearn.ensemble import RandomForestRegressor
import joblib
import os
from utils.logger import setup_logger

class ValuationModel:
    """
    Machine learning model for NFT valuation.
    """

    def __init__(self, config):
        self.model_path = config.get('model_path', 'data/models/model_v1.pkl')
        self.logger = setup_logger(config.get('logging', {}))
        self.model = self._load_model()

    def _load_model(self):
        if os.path.exists(self.model_path):
            self.logger.info(f"Loading model from {self.model_path}")
            return joblib.load(self.model_path)
        else:
            self.logger.error(f"Model file not found at {self.model_path}")
            raise FileNotFoundError("Model file not found")

    def predict(self, features):
        self.logger.debug(f"Predicting valuation with features: {features}")
        input_data = self._prepare_input(features)
        prediction = self.model.predict([input_data])[0]
        self.logger.debug(f"Prediction result: {prediction}")
        return prediction

    def get_latest(self, nft_id):
        self.logger.debug(f"Retrieving latest valuation for NFT ID: {nft_id}")
        # Placeholder for retrieving the latest valuation from the database or another source
        # This should be implemented based on the actual data storage
        return 1000  # Example value

    def _prepare_input(self, features):
        # Convert features dictionary to a list or array as required by the model
        input_list = [
            features.get('rarity', 0),
            len(features.get('historical_prices', [])),
            features.get('market_trends', {}).get('trend', 0),
            1 if features.get('sentiment') == 'positive' else -1
        ]
        self.logger.debug(f"Prepared input for model: {input_list}")
        return input_list