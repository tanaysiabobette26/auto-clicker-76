import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional


class AutoclickerLogFormatter(logging.Formatter):
    """Custom log formatter injecting click glyphs and telemetry info."""

    GLYPHS = {"INFO": "⚡", "WARNING": "⚠️", "ERROR": "💥", "DEBUG": "🔍"}

    def format(self, record: logging.LogRecord) -> str:
        record.glyph = self.GLYPHS.get(record.levelname, "📌")
        if not hasattr(record, "click_rate"):
            record.click_rate = 0.0
        return super().format(record)


def setup_click_logger(
    log_file: str = "logs/autoclicker.log",
    max_bytes: int = 256 * 1024,
    backup_count: int = 5,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures a rotating logger with burst telemetry support for auto-clicker-76."""
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("autoclicker76")
    logger.setLevel(level)
    logger.handlers.clear()

    log_format = "[%(asctime)s] %(glyph)s [%(levelname)s] [CPS: %(click_rate).1f] %(message)s"
    formatter = AutoclickerLogFormatter(fmt=log_format, datefmt="%H:%M:%S")

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info("Auto-clicker rotation logging engine active", extra={"click_rate": 0.0})
    return logger


def log_click_event(logger: logging.Logger, cps: float, total_clicks: int, target: str = "active_window") -> None:
    """Emits structured log metrics during automated click bursts."""
    logger.info(
        f"Pulse fired -> target={target} total_clicks={total_clicks}",
        extra={"click_rate": cps},
    )
