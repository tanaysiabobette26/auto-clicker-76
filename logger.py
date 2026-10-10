import sys
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class ClickDiagnosticsFilter(logging.Filter):
    """Injects autoclicker runtime sequence and window context into logs."""
    def __init__(self, target_window: str = "Active Window"):
        super().__init__()
        self.target_window = target_window
        self.click_sequence = 0

    def filter(self, record: logging.LogRecord) -> bool:
        self.click_sequence += 1
        record.seq = f"#{self.click_sequence:06d}"
        record.window = self.target_window
        return True

def setup_autoclick_logger(
    log_file: str = "autoclicker.log",
    max_bytes: int = 1_048_576,
    backup_count: int = 5,
    target_name: str = "Main Target"
) -> logging.Logger:
    """Configures a high-frequency rotating logger for auto-clicker events."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    full_path = log_dir / log_file

    logger = logging.getLogger("AutoClicker76")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    file_handler = RotatingFileHandler(
        full_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_formatter = logging.Formatter(
        "[%(asctime)s] [%(seq)s] [%(levelname)s] [%(window)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter("⚡ [%(levelname)s] %(message)s")
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)

    logger.addFilter(ClickDiagnosticsFilter(target_window=target_name))
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info(f"Logger initialized at {full_path.name}")
    return logger

if __name__ == "__main__":
    log = setup_autoclick_logger()
    log.info("Autoclicker engine session started")
    log.debug("Initial click position: x=500, y=300")
