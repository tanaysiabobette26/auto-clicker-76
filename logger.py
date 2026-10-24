import logging
import sys
from typing import Final

LOG_FORMAT: Final[str] = "%(asctime)s | %(levelname)-8s | %(message)s"

def setup_logger(name: str = "auto-clicker-76") -> logging.Logger:
    """
    Initialize a logger instance with custom formatting for debugging.
    
    :param name: Identifier for the logger.
    :return: Configured logging.Logger object.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        stream_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(LOG_FORMAT)
        
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

class ClickerLogger:
    """
    A wrapper for logging application events during clicking tasks.
    """
    def __init__(self, log_name: str = "auto-clicker-76") -> None:
        self.logger: logging.Logger = setup_logger(log_name)

    def info(self, msg: str) -> None:
        """Log an informational message."""
        self.logger.info(msg)

    def warn(self, msg: str) -> None:
        """Log a warning message."""
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """Log a critical error message."""
        self.logger.error(msg)