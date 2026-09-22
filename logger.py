import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='auto-clicker-76', log_file='app.log', level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(module)s:%(lineno)d | %(message)s'
        )
        
        # Rotating file handler: 5MB per file, keeps 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        
        logger.addHandler(handler)
        logger.addHandler(console)
    
    return logger

# Instantiate a singleton-style logger for the application
clicker_logger = setup_logger()