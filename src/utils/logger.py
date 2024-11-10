import logging
import sys

def setup_logger(config):
    """
    Sets up and returns a logger based on the provided configuration.
    """
    logger = logging.getLogger(config.get('name', 'nft_valuation_advisor'))
    logger.setLevel(config.get('level', 'INFO').upper())

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(config.get('level', 'INFO').upper())
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    if 'file' in config:
        fh = logging.FileHandler(config['file'])
        fh.setLevel(config.get('level', 'INFO').upper())
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger