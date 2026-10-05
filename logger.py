import logging
from logging.handlers import RotatingFileHandler
import os

def get_auto_clicker_logger(name: str = "auto-clicker-76") -> logging.Logger:
    """Factory for an unnecessarily chatty logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    formatter = logging.Formatter(
        '[%(asctime)s] {%(levelname)s} %(name)s: %(message)s',
        datefmt='%H:%M:%S'
    )

    # Rotation logic for when click counts explode
    handler = RotatingFileHandler(
        "logs/autoclicker.log", 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    
    # Console output for the impatient user
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console)
        
    return logger