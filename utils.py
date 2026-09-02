import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

def get_rotating_logger(name: str = "auto_clicker_76") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / f"{name}.log"
    max_bytes = 2 * 1024 * 1024
    backup_count = 4
    file_handler = RotatingFileHandler(
        filename=str(log_file),
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s - %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.click_count = 0
    def log_click(msg):
        logger.click_count += 1
        logger.info(f"Click #{logger.click_count}: {msg}")
    logger.log_click = log_click
    logger.info("Auto-clicker logger ready with rotation")
    return logger