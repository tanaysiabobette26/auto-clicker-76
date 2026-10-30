import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path('logs')
LOG_FILE = LOG_DIR / 'clicker.log'

class ClickerFormatter(logging.Formatter):
    _styles = {
        logging.DEBUG: '🔍',
        logging.INFO: '⚡',
        logging.WARNING: '⚠️',
        logging.ERROR: '💀',
        logging.CRITICAL: '🔥'
    }

    def format(self, record):
        icon = self._styles.get(record.levelno, '🤖')
        record.msg = f'{icon} {record.msg}'
        return super().format(record)

def setup_logger():
    LOG_DIR.mkdir(exist_ok=True)
    
    handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1024 * 512,
        backupCount=3,
        encoding='utf-8'
    )
    
    formatter = ClickerFormatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
    handler.setFormatter(formatter)
    
    logger = logging.getLogger('auto-clicker-76')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    
    return logger

logger = setup_logger()