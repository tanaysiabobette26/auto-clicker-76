import gzip
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import shutil
import time

class ClickContextFilter(logging.Filter):
    """Injects high-precision delta time since last click event and custom icons."""
    def __init__(self):
        super().__init__()
        self.last_log_time = time.perf_counter()

    def filter(self, record):
        now = time.perf_counter()
        record.delta_ms = (now - self.last_log_time) * 1000
        self.last_log_time = now
        
        emojis = {
            logging.DEBUG: "🔍", 
            logging.INFO: "🖱️", 
            logging.WARNING: "⚠️", 
            logging.ERROR: "💥"
        }
        record.emoji = emojis.get(record.levelno, "⚙️")
        return True

def setup_logger(log_dir: str = "logs", log_name: str = "clicker.log") -> logging.Logger:
    path = Path(log_dir)
    path.mkdir(exist_ok=True)
    log_path = path / log_name

    logger = logging.getLogger("auto-clicker-76")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if not logger.handlers:
        def gz_namer(name: str) -> str:
            return f"{name}.gz"

        def gz_rotator(source: str, dest: str) -> None:
            with open(source, "rb") as f_in:
                with gzip.open(dest, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
            if os.path.exists(source):
                os.remove(source)

        # Rotate at 100 KB, keeping last 5 backups compressed
        file_handler = RotatingFileHandler(
            log_path, maxBytes=100 * 1024, backupCount=5, encoding="utf-8"
        )
        file_handler.namer = gz_namer
        file_handler.rotator = gz_rotator
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            fmt="[%(asctime)s.%(msecs)03d] %(emoji)s [%(levelname)s] (dt: %(delta_ms).1fms) %(message)s",
            datefmt="%H:%M:%S"
        )

        for handler in (file_handler, console_handler):
            handler.addFilter(ClickContextFilter())
            handler.setFormatter(formatter)
            logger.addHandler(handler)

    return logger