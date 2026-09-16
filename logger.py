import logging
from logging.handlers import RotatingFileHandler
import sys
import os

def get_auto_clicker_logger(name: str = "auto-clicker-76"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
        datefmt='%H:%M:%S'
    )

    # Console stream for instant feedback
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotation logic: 1MB per file, keep 3 backups
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    file_path = os.path.join(log_dir, "activity.log")
    file_handler = RotatingFileHandler(
        file_path, 
        maxBytes=1024 * 1024, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        logger.propagate = False
        
    return logger

# Singleton instance for the clicker
clicker_logger = get_auto_clicker_logger()