from src.exception import CustException
from src.logger import logging


def read_prompt(file_path):
    """ This function is used to read the text file 
    """
    try:
        logging.info("inside read_prompt function")
        with open(file_path, 'r') as file:
            content = file.read().replace('\n', ' ')
            return content
    except FileNotFoundError:
        logging.info(f"The file '{file_path}' does not exist.")
    except Exception as e:
        logging.info(f"An error occurred: {e}")
