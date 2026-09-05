import logging
import sys
from datetime import datetime

class ClickerLogger:
    def __init__(self, name="auto-clicker-76"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self._setup_streams()

    def _setup_streams(self):
        formatter = logging.Formatter(
            "[%(asctime)s | %(levelname)s] %(message)s", 
            datefmt="%H:%M:%S"
        )
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        self.logger.addHandler(stdout_handler)

    def info(self, msg):
        self.logger.info(f"✨ {msg}")

    def warn(self, msg):
        self.logger.warning(f"⚠️ {msg}")

    def error(self, msg):
        self.logger.error(f"💥 {msg}")

    def debug(self, msg):
        self.logger.debug(f"🔎 {msg}")

logger = ClickerLogger()