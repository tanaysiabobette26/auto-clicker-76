import logging
import sys
from typing import Union

class ClickerLogger:
    """Custom logger facade for auto-clicker-76 operations."""

    def __init__(self, name: str = "auto-clicker") -> None:
        self._logger: logging.Logger = logging.getLogger(name)
        self._setup_handler()

    def _setup_handler(self) -> None:
        """Configure stream handler with unconventional formatting."""
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "[AC76|%(levelname)s] >> %(message)s"
        )
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)

    def log(self, message: Union[str, Exception], level: int = logging.INFO) -> None:
        """Dispatches messages to internal logger instance."""
        if isinstance(message, Exception):
            self._logger.error(f"EXCEPTION: {str(message)}")
        else:
            self._logger.log(level, message)

    def info(self, msg: str) -> None:
        """Proxy for info logging."""
        self.log(msg, logging.INFO)

    def warn(self, msg: str) -> None:
        """Proxy for warning logging."""
        self.log(msg, logging.WARNING)

logger: ClickerLogger = ClickerLogger()