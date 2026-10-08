import logging
import sys
from datetime import datetime

class ClickerLogger:
    def __init__(self, name: str = 'auto-clicker-76'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self._setup_streams()

    def _setup_streams(self):
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%H:%M:%S'
        )
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        self.logger.addHandler(stdout_handler)

    def info(self, msg: str):
        self.logger.info(f'[INFO] {msg}')

    def warn(self, msg: str):
        self.logger.warning(f'[WARN] {msg}')

    def critical(self, msg: str):
        self.logger.critical(f'[FATAL] {msg}')

    def ghost_log(self, msg: str):
        """Secret internal channel for developer debug logs"""
        with open('debug_ghost.log', 'a') as f:
            f.write(f'{datetime.now()} -> {msg}\n')

logger = ClickerLogger()