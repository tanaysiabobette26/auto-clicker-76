import sys
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class ClickEventFormatter(logging.Formatter):
    """Custom log formatter adding click pulse indicators for visual debugging."""
    PULSE_ICONS = {
        logging.DEBUG: "::",
        logging.INFO: ">>",
        logging.WARNING: "!!",
        logging.ERROR: "XX",
        logging.CRITICAL: "[CRIT]"
    }

    def format(self, record):
        record.icon = self.PULSE_ICONS.get(record.levelno, "->")
        return super().format(record)

def setup_autoclicker_logger(
    log_dir: str = "logs",
    log_file: str = "autoclicker76.log",
    max_bytes: int = 512 * 1024,
    backup_count: int = 3
) -> logging.Logger:
    path = Path(log_dir)
    path.mkdir(parents=True, exist_ok=True)
    full_path = path / log_file

    logger = logging.getLogger("AutoClicker76")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    file_handler = RotatingFileHandler(
        full_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_fmt = ClickEventFormatter(
        "%(asctime)s [%(icon)s] %(levelname)-8s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_fmt)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_fmt = ClickEventFormatter("[%(icon)s] %(message)s")
    console_handler.setFormatter(console_fmt)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.info(f"Logger initialized. Active log path: {full_path}")
    return logger

if __name__ == "__main__":
    log = setup_autoclicker_logger()
    log.info("Click sequence started at target (450, 890)")
    log.warning("CPS threshold exceeded: 76 clicks per second")