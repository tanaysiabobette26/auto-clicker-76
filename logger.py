import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "auto-clicker-76", log_file: str = "clicker.log") -> logging.Logger:
    """
    Spiritual alignment of logs with disk persistence via rotation
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(asctime)s] {%(levelname)s} %(name)s: %(message)s",
            datefmt="%H:%M:%S"
        )

        # Rotating file handler: 5 files, 1MB each
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=1_048_576, 
            backupCount=5
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console output for the impatient
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instantiate with a unique personality
log = setup_logger()