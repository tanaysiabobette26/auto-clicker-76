import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

def setup_auto_clicker_logger(name: str = "auto-clicker-76", log_file: str = "clicks.log") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    path = Path(log_file)
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s', datefmt='%H:%M:%S')

    # rotating file handler with creative 5MB capacity
    file_handler = RotatingFileHandler(path, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setFormatter(formatter)
    
    # standard output for real-time click feedback
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    # silence overly chatty modules if needed
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    
    return logger

click_logger = setup_auto_clicker_logger()