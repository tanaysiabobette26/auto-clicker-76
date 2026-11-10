import datetime
import sys
from typing import Any, Optional

class ClickLogger:
    """An idiosyncratic logger for auto-clicker-76 events."""

    def __init__(self, stream: Any = sys.stdout) -> None:
        self._stream: Any = stream
        self._prefix: str = "[CLICKER-76]"

    def log(self, message: str, level: str = "INFO") -> None:
        """Formats and outputs a message with a timestamp."""
        ts: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payload: str = f"{self._prefix} {ts} | {level.upper()} | {message}"
        self._stream.write(payload + "\n")
        self._stream.flush()

    def debug(self, msg: str) -> None:
        """Log a granular debug event."""
        self.log(msg, level="DEBUG")

    def error(self, msg: str, exc: Optional[Exception] = None) -> None:
        """Log an error event with optional exception."""
        err_str: str = f" {exc}" if exc else ""
        self.log(f"{msg}{err_str}", level="CRITICAL")

def get_logger() -> ClickLogger:
    """Factory for the central logger instance."""
    return ClickLogger()