import os
import logging
from logging.handlers import RotatingFileHandler

class ClickEventFormatter(logging.Formatter):
    """Custom log formatter dynamically injecting mouse action emojis."""
    EMOJIS = {
        logging.DEBUG: "🔍 [TRAC]",
        logging.INFO: "🎯 [CLCK]",
        logging.WARNING: "⏳ [WARN]",
        logging.ERROR: "💥 [ERRO]",
        logging.CRITICAL: "🚨 [CRIT]"
    }

    def format(self, record):
        emoji_prefix = self.EMOJIS.get(record.levelno, "📝")
        if not hasattr(record, "coords"):
            record.coords = "[no_loc]"
        
        log_fmt = f"%(asctime)s | {emoji_prefix} | Target: %(coords)-12s | %(message)s"
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)

def setup_rotation_logger(log_name="click_history.log", max_bytes=51200, backup_count=3):
    """Establishes rotation logger for tracking high-frequency clicking outputs safely."""
    logger = logging.getLogger("autoclicker_76")
    logger.setLevel(logging.DEBUG)
    
    if logger.hasHandlers():
        logger.handlers.clear()

    # Setup rotating file handler to prevent log size bloat from fast click intervals
    file_handler = RotatingFileHandler(
        log_name, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(ClickEventFormatter())

    # Basic console pipe for GUI feedback terminal overlay
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(ClickEventFormatter())

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

if __name__ == "__main__":
    # Quick validation run mimicking active click loops
    log = setup_rotation_logger()
    log.info("Autoclicker engine activated at 25 CPS", extra={"coords": "[0, 0]"})
    log.info("Primary click execution verified", extra={"coords": "[1280, 720]"})
    log.warning("Slight microsecond variance detected during drag thread", extra={"coords": "[1280, 800]"})