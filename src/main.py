import argparse
import sys
from src.app import app
from utils.logger import setup_logger
from utils.config_loader import ConfigLoader

def parse_arguments():
    parser = argparse.ArgumentParser(description="NFT Valuation Advisor CLI")
    parser.add_argument('--config', type=str, default='configs/config.yaml', help='Path to configuration file')
    parser.add_argument('--host', type=str, help='Host address to run the server')
    parser.add_argument('--port', type=int, help='Port number to run the server')
    parser.add_argument('--debug', action='store_true', help='Run the server in debug mode')
    return parser.parse_args()

def main():
    args = parse_arguments()
    config = ConfigLoader.load_config(args.config)
    
    if args.host:
        config['server']['host'] = args.host
    if args.port:
        config['server']['port'] = args.port
    if args.debug:
        config['logging']['level'] = 'DEBUG'
    
    logger = setup_logger(config['logging'])
    logger.info("Starting NFT Valuation Advisor Application")
    
    try:
        app.run(host=config['server']['host'], port=config['server']['port'], debug=args.debug)
    except Exception as e:
        logger.exception(f"Failed to start the application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()