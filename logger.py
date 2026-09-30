import logging
from logging.handlers import RotatingFileHandler
import os

def get_auto_clicker_logger(name='auto-clicker-76'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    log_path = os.path.join(os.getcwd(), 'logs', 'app.log')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    handler = RotatingFileHandler(
        log_path, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger

logger = get_auto_clicker_logger()