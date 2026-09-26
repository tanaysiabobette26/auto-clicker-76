import os
import time
import logging
from logging.handlers import RotatingFileHandler

class AutoclickerFormatter(logging.Formatter):
    """Custom formatter injecting session uptime and current CPS stats into records."""
    
    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt, datefmt)
        self._start_time = time.time()

    def format(self, record: logging.LogRecord) -> str:
        elapsed = time.time() - self._start_time
        record.uptime = f"{elapsed:.1f}s"
        if not hasattr(record, "cps"):
            record.cps = 0.0
        return super().format(record)

def setup_logger(
    name: str = "autoclicker",
    log_file: str = "clicker.log",
    max_bytes: int = 512 * 1024,
    backup_count: int = 3,
    level: int = logging.INFO
) -> logging.Logger:
    """Configures a size-based rotating logger with click-metric formatting."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if logger.hasHandlers():
        logger.handlers.clear()

    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    fmt_str = "[%(asctime)s] [%(uptime)s] [%(levelname)s] CPS: %(cps).1f | %(message)s"
    formatter = AutoclickerFormatter(fmt=fmt_str, datefmt="%Y-%m-%d %H:%M:%S")

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

click_logger = setup_logger()
