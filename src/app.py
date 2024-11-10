import os
from flask import Flask, jsonify, request
from services.valuation_service import ValuationService
from services.user_service import UserService
from utils.logger import setup_logger
from utils.config_loader import ConfigLoader

config = ConfigLoader.load_config('configs/config.yaml')
logger = setup_logger(config['logging'])

app = Flask(__name__)
valuation_service = ValuationService(config)
user_service = UserService(config)

@app.route('/api/valuate', methods=['POST'])
def valuate_nft():
    data = request.json
    user_id = data.get('user_id')
    nft_id = data.get('nft_id')
    if not user_id or not nft_id:
        logger.error("Missing user_id or nft_id in request")
        return jsonify({'error': 'Missing user_id or nft_id'}), 400
    try:
        user = user_service.get_user(user_id)
        nft = valuation_service.get_nft_details(nft_id)
        valuation = valuation_service.calculate_valuation(nft, user)
        logger.info(f"Valuation calculated for NFT {nft_id} by User {user_id}")
        return jsonify({'valuation': valuation}), 200
    except Exception as e:
        logger.exception("Error during valuation process")
        return jsonify({'error': str(e)}), 500

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.json
    try:
        user = user_service.create_user(data)
        logger.info(f"User created with ID {user.id}")
        return jsonify({'user_id': user.id}), 201
    except Exception as e:
        logger.exception("Error creating user")
        return jsonify({'error': str(e)}), 500

@app.route('/api/nft', methods=['POST'])
def add_nft():
    data = request.json
    try:
        nft = valuation_service.add_nft(data)
        logger.info(f"NFT added with ID {nft.id}")
        return jsonify({'nft_id': nft.id}), 201
    except Exception as e:
        logger.exception("Error adding NFT")
        return jsonify({'error': str(e)}), 500

@app.route('/api/valuation/<nft_id>', methods=['GET'])
def get_valuation(nft_id):
    try:
        valuation = valuation_service.get_latest_valuation(nft_id)
        if valuation:
            return jsonify({'valuation': valuation}), 200
        else:
            return jsonify({'error': 'Valuation not found'}), 404
    except Exception as e:
        logger.exception("Error retrieving valuation")
        return jsonify({'error': str(e)}), 500

@app.route('/api/report/<user_id>', methods=['GET'])
def generate_report(user_id):
    try:
        report = valuation_service.generate_user_report(user_id)
        return jsonify({'report': report}), 200
    except Exception as e:
        logger.exception("Error generating report")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config['server']['port'])