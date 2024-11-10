import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os
from utils.logger import setup_logger

class PricingModel:
    """
    Machine Learning model for predicting NFT prices based on various features.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.model_path = config.get('model_path', 'data/models/pricing_model.pkl')
        self.model = self._load_model()
        self.logger.info("Pricing Model initialized.")

    def _load_model(self):
        if os.path.exists(self.model_path):
            self.logger.info(f"Loading pricing model from {self.model_path}")
            return joblib.load(self.model_path)
        else:
            self.logger.warning(f"Pricing model not found at {self.model_path}. Initializing a new model.")
            return LinearRegression()

    def train(self, data_path):
        """
        Train the pricing model using the provided dataset.

        Args:
            data_path (str): Path to the CSV dataset.
        """
        self.logger.info(f"Loading training data from {data_path}")
        data = pd.read_csv(data_path)
        self.logger.debug(f"Training data shape: {data.shape}")

        X = data.drop('price', axis=1)
        y = data['price']

        self.logger.info("Splitting data into training and testing sets.")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.logger.info("Training the pricing model.")
        self.model.fit(X_train, y_train)

        score = self.model.score(X_test, y_test)
        self.logger.info(f"Model training completed with R^2 score: {score}")

        self.save_model()

    def predict(self, features):
        """
        Predict the price of an NFT based on its features.

        Args:
            features (dict): Dictionary of NFT features.

        Returns:
            float: Predicted price.
        """
        self.logger.debug(f"Predicting price with features: {features}")
        feature_values = np.array([features[key] for key in sorted(features.keys())]).reshape(1, -1)
        prediction = self.model.predict(feature_values)[0]
        self.logger.debug(f"Predicted price: {prediction}")
        return prediction

    def save_model(self):
        """
        Save the trained model to disk.
        """
        self.logger.info(f"Saving pricing model to {self.model_path}")
        joblib.dump(self.model, self.model_path)
        self.logger.info("Pricing model saved successfully.")

    def evaluate(self, data_path):
        """
        Evaluate the model performance on a test dataset.

        Args:
            data_path (str): Path to the CSV dataset.

        Returns:
            float: R^2 score of the model.
        """
        self.logger.info(f"Loading evaluation data from {data_path}")
        data = pd.read_csv(data_path)
        X = data.drop('price', axis=1)
        y = data['price']

        self.logger.info("Evaluating the pricing model.")
        score = self.model.score(X, y)
        self.logger.info(f"Model evaluation completed with R^2 score: {score}")
        return score