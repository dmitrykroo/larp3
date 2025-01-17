import hashlib
import json
from utils.logger import setup_logger

def generate_unique_id(data):
    """
    Generate a unique SHA-256 hash ID based on the input data.

    Args:
        data (dict): Input data to hash.

    Returns:
        str: Unique hash ID.
    """
    logger = setup_logger({})
    logger.debug(f"Generating unique ID for data: {data}")
    data_string = json.dumps(data, sort_keys=True)
    unique_id = hashlib.sha256(data_string.encode()).hexdigest()
    logger.debug(f"Generated unique ID: {unique_id}")
    return unique_id

def load_json(file_path):
    """
    Load JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON data.
    """
    logger = setup_logger({})
    logger.debug(f"Loading JSON data from {file_path}")
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        logger.debug("JSON data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load JSON data: {e}")
        return {}

def save_json(data, file_path):
    """
    Save data as JSON to a file.

    Args:
        data (dict): Data to save.
        file_path (str): Path to the output JSON file.
    """
    logger = setup_logger({})
    logger.debug(f"Saving JSON data to {file_path}")
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        logger.debug("JSON data saved successfully.")
    except Exception as e:
        logger.error(f"Failed to save JSON data: {e}")

def calculate_hash(data):
    """
    Calculate SHA-256 hash of the input data.

    Args:
        data (str): Input data as string.

    Returns:
        str: SHA-256 hash.
    """
    logger = setup_logger({})
    logger.debug(f"Calculating SHA-256 hash for data: {data}")
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    logger.debug(f"Calculated hash: {sha256_hash}")
    return sha256_hash
                                                                
                                                                
                                                                
                                                                
                                                                
                                                              
                                                              
                                                              
                                                              
                                                              

























