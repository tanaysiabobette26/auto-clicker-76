import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

def setup_autoclicker_logger(name: str = 'auto-clicker-76') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    log_path = Path('logs')
    log_path.mkdir(exist_ok=True)
    file_path = log_path / f'{name}.log'
    
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] %(message)s',
        datefmt='%H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        file_path, 
        maxBytes=1024 * 512, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

# Instantiate for global access
log = setup_autoclicker_logger()