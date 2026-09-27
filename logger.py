import logging
from logging.handlers import RotatingFileHandler
import sys
import os

def setup_autoclicker_logger(name='auto-clicker-76', log_file='autoclicker.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(process)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024*1024*5, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info('system logging initialized for auto-clicker-76')
    return logger

log = setup_autoclicker_logger()