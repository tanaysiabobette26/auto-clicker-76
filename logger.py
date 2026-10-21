import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

class ClickPulseFormatter(logging.Formatter):
    """Custom formatter adding dynamic visual indicators for click activities."""
    PULSES = ["·", "•", "●", "✦", "█"]

    def format(self, record: logging.LogRecord) -> str:
        cps = getattr(record, 'cps', 0)
        idx = min(int(cps / 10), len(self.PULSES) - 1)
        record.pulse = self.PULSES[idx] if cps > 0 else " "
        return super().format(record)

def setup_autoclick_logger(
    log_file: str = "autoclicker.log",
    max_bytes: int = 512 * 1024,
    backup_count: int = 3,
    level: int = logging.INFO
) -> logging.Logger:
    """Configures rotating logger tailored for high-frequency click events."""
    logger = logging.getLogger("auto_clicker_76")
    logger.setLevel(level)

    if logger.handlers:
        return logger

    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    fmt = "[%(asctime)s] [%(levelname)s] [%(pulse)s] %(message)s"
    formatter = ClickPulseFormatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    log = setup_autoclick_logger("logs/clicker.log")
    log.info("Autoclicker initialized", extra={"cps": 0})
    log.info("Click burst active", extra={"cps": 25})
