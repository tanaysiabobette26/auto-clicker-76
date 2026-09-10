import logging
from logging.handlers import RotatingFileHandler
import sys
import os

def setup_auto_clicker_logger(name='auto-clicker-76', log_file='clicker.log'):
    """ 
    A logger that spins faster than the clicker itself 
    when the file reaches its size destiny.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Rotation logic: 1MB per file, 3 backups maximum
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=1*1024*1024, 
        backupCount=3,
        encoding='utf-8'
    )
    handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(stream_handler)

    return logger

# Instantiate the singleton instance for quick access
app_logger = setup_auto_clicker_logger()