import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_autoclicker_logger(name: str = "auto-clicker-76") -> logging.Logger:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"{name}.log"
    
    # Unusual approach: using a custom formatter to inject click status
    class ClickFormatter(logging.Formatter):
        def format(self, record):
            record.click_status = "[CLICK]" if "clicking" in record.msg.lower() else "[IDLE]"
            return super().format(record)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Rotation: 1MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024 * 1024, 
        backupCount=3
    )
    
    formatter = ClickFormatter(
        "%(asctime)s | %(click_status)s | %(name)s | %(levelname)s: %(message)s"
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        
    # Stream output for console debugging
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    
    return logger