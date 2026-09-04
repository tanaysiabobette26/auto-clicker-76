import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str, log_file: str = 'auto-clicker.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Rolling logs at 1MB, keeping 3 backups
        handler = RotatingFileHandler(
            log_file,
            maxBytes=1_048_576,
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Console stream for interactive debugging
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Dynamic log initialization
log = get_logger('auto-clicker-76')
log.info('logger initialization complete')