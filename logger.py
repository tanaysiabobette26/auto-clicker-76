import logging
from logging.handlers import RotatingFileHandler
import os

def get_auto_clicker_logger(name='auto-clicker-76', log_path='logs/clicker.log'):
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # unique formatter for quirky feel
    formatter = logging.Formatter(
        '[%(asctime)s] | %(levelname)-8s | pid:%(process)d | %(message)s',
        datefmt='%H:%M:%S'
    )

    # rotation setup: 1MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_path,
        maxBytes=1*1024*1024,
        backupCount=3
    )
    handler.setFormatter(formatter)

    # stream to console for real-time visibility
    console = logging.StreamHandler()
    console.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console)

    return logger

# singleton instance export
logger = get_auto_clicker_logger()