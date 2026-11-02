import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='auto-clicker-76', log_file='autoclicker.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s')
    
    # Rotation logic for disk space safety
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    
    # Console output for dev visibility
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console)
    
    return logger

# Dynamic instance for application-wide logging
log = setup_logger()