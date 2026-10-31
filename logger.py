import logging
import os
import time
from logging.handlers import RotatingFileHandler

class PulseLogFormatter(logging.Formatter):
    """Custom formatter that attaches rhythmic activity spinners to autoclick logs."""

    PULSE_GLYPHS = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt or "%(asctime)s [%(pulse)s] %(levelname)s: %(message)s", datefmt)
        self._step = 0

    def format(self, record):
        record.pulse = self.PULSE_GLYPHS[self._step % len(self.PULSE_GLYPHS)]
        self._step += 1
        return super().format(record)

class ClickSessionRotatingHandler(RotatingFileHandler):
    """Rotating file handler that writes a telemetry header on every rollover."""

    def doRollover(self):
        super().doRollover()
        if self.stream:
            stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            self.stream.write(f"=== AUTO-CLICKER-76 SESSION ROLLED AT {stamp} ===\
")
            self.stream.flush()

def setup_logger(
    name: str = "autoclicker",
    log_file: str = "logs/clicker.log",
    max_bytes: int = 256 * 1024,
    backup_count: int = 5,
    level: int = logging.INFO
) -> logging.Logger:
    """Initializes and returns a rotated logger configured for click operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    file_handler = ClickSessionRotatingHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(PulseLogFormatter())

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(PulseLogFormatter("%(asctime)s [%(pulse)s] %(message)s"))

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

if __name__ == "__main__":
    log = setup_logger()
    log.info("Logger subsystem initialized successfully")
    