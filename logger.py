import logging
from logging.handlers import RotatingFileHandler
import sys
import os

class AutoClickerLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AutoClickerLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, log_file='autoclicker.log'):
        if hasattr(self, '_initialized'):
            return
        self.logger = logging.getLogger('auto-clicker-76')
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s'
        )

        file_handler = RotatingFileHandler(
            log_file, maxBytes=1024 * 1024 * 5, backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        self._initialized = True

    def get_logger(self):
        return self.logger

logger_instance = AutoClickerLogger().get_logger()