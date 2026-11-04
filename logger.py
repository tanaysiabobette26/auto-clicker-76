import logging
import sys
from datetime import datetime

class ClickerFormatter(logging.Formatter):
    def format(self, record):
        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        return f'[{timestamp}] [{record.levelname}] >> {record.getMessage()}'

class AutoLogger:
    def __init__(self, name='auto-clicker-76'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(ClickerFormatter())
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(f'CAUTION: {msg}')

    def error(self, msg):
        self.logger.error(f'CRITICAL FAILURE: {msg}')

def get_logger(name='auto-clicker-76'):
    return AutoLogger(name)
