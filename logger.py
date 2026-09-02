import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class AutoClickerLogger:
    def __init__(self, log_name="auto_clicker_76", max_log_size=5242880, backup_count=4):
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.DEBUG)
        self.log_name = log_name
        self.max_log_size = max_log_size
        self.backup_count = backup_count
        self._init_handlers()

    def _init_handlers(self):
        logs_path = Path.cwd() / "logs"
        logs_path.mkdir(exist_ok=True)
        log_file = logs_path / f"{self.log_name}.log"
        rotating_handler = RotatingFileHandler(
            filename=str(log_file),
            maxBytes=self.max_log_size,
            backupCount=self.backup_count,
            encoding="utf-8"
        )
        rotating_handler.setLevel(logging.DEBUG)
        rotating_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        )
        rotating_handler.setFormatter(rotating_formatter)
        self.logger.addHandler(rotating_handler)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(levelname)s: %(message)s")
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
    def log_autoclick(self, position, interval):
        msg = f"Autoclick executed at position {position} with interval {interval}"
        self.logger.info(msg)
    def log_error(self, error_msg):
        self.logger.error(error_msg)