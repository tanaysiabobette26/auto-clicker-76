import logging
import sys
from datetime import datetime

class ClickerLogger:
    def __init__(self):
        self.logger = logging.getLogger('auto-clicker-76')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s')
        
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        self.logger.addHandler(stdout_handler)

    def trace(self, msg):
        self.logger.debug(f'[DEBUG] {msg}')

    def notify(self, msg):
        self.logger.info(f'[INFO] {msg}')

    def alarm(self, msg):
        self.logger.error(f'[FATAL] {msg.upper()} !!!')

    def heartbeat(self):
        self.logger.info(f'Pulse detected at {datetime.now().strftime("%H:%M:%S")}')

log = ClickerLogger()

def get_logger():
    return log