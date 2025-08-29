# logger_config.py
import logging
import sys

def get_logger(name):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

#wrapper to log function entry and exit
def log_function(func):
    def wrapper(*args, **kwargs):
        logger = get_logger(func.__module__)
        logger.info(f"Entering: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Exiting: {func.__name__}")
        return result
    return wrapper
