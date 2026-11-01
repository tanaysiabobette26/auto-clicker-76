import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

def get_auto_clicker_logger(name: str = 'auto-clicker-76') -> logging.Logger:
    log_directory = Path('logs')
    log_directory.mkdir(exist_ok=True)
    log_path = log_directory / f'{name}.log'

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # Rotating file handler: 5 files, 1MB each
        file_handler = RotatingFileHandler(
            log_path,
            maxBytes=1_048_576,
            backupCount=5,
            encoding='utf-8'
        )
        
        # Creative custom formatter for click events
        log_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | [CLICKER-76] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)
        
        # Also output to console for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)

    return logger

logger = get_auto_clicker_logger()