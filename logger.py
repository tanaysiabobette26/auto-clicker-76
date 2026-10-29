import logging
import os
from logging.handlers import RotatingFileHandler
from time import time


class HighFrequencyLogFilter(logging.Filter):
    """Throttles rapid click log output to prevent disk thrashing."""

    def __init__(self, burst_threshold_sec: float = 0.05):
        super().__init__()
        self.burst_threshold = burst_threshold_sec
        self.last_log_time = 0.0

    def filter(self, record: logging.LogRecord) -> bool:
        if getattr(record, "is_click_pulse", False):
            now = time()
            if now - self.last_log_time < self.burst_threshold:
                return False
            self.last_log_time = now
        return True


def setup_autoclick_logger(
    name: str = "autoclicker",
    log_file: str = "logs/clicker.log",
    max_bytes: int = 1_048_576,
    backup_count: int = 3,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures a rotating log handler tailored for high-speed autoclicker metrics."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if logger.hasHandlers():
        return logger

    log_dir = os.path.dirname(os.path.abspath(log_file))
    os.makedirs(log_dir, exist_ok=True)

    formatter = logging.Formatter(
        fmt="[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    filter_instance = HighFrequencyLogFilter()

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.addFilter(filter_instance)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.addFilter(filter_instance)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Clicker telemetry logger initialized with rotation")
    return logger
