import logging
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path


class AutoClickerFormatter(logging.Formatter):
    """Custom log formatter decorating click events with dynamic markers."""

    PULSE_ICONS = {
        logging.DEBUG: "⚡",
        logging.INFO: "🎯",
        logging.WARNING: "⚠️",
        logging.ERROR: "💥",
        logging.CRITICAL: "☠️",
    }

    def format(self, record: logging.LogRecord) -> str:
        record.pulse_icon = self.PULSE_ICONS.get(record.levelno, "📌")
        record.click_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        return super().format(record)


def setup_logger(
    log_dir: str = "logs",
    max_bytes: int = 512 * 1024,
    backup_count: int = 5,
    level: int = logging.DEBUG,
) -> logging.Logger:
    """Initializes a rotating logger configured for high-frequency click tracking."""
    target_dir = Path(log_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    log_file = target_dir / "autoclicker_session.log"

    logger = logging.getLogger("auto_clicker_76")
    logger.setLevel(level)

    if logger.hasHandlers():
        logger.handlers.clear()

    pattern = "[%(click_timestamp)s] [%(pulse_icon)s %(levelname)s] [%(filename)s:%(lineno)d] %(message)s"
    formatter = AutoClickerFormatter(pattern)

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Logger rotation configured (%d KB limit)", max_bytes // 1024)
    return logger


click_logger = setup_logger()
