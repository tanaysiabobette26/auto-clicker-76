import logging
import sys
from typing import Final, Optional

class ClickerLogger:
    """
    A vibrant logger for auto-clicker-76 events.
    """
    FORMAT: Final[str] = "%(asctime)s | %(levelname)s | %(message)s"
    
    def __init__(self, name: str = "auto-clicker") -> None:
        self._logger: logging.Logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)
        self._handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        self._handler.setFormatter(logging.Formatter(self.FORMAT))
        self._logger.addHandler(self._handler)

    def info(self, msg: str, data: Optional[dict] = None) -> None:
        """
        Logs informational clicks or lifecycle transitions.
        """
        full_msg: str = f"{msg} {data if data else ''}"
        self._logger.info(full_msg)

    def warn(self, reason: str) -> None:
        """
        Logs non-fatal hiccups in the click flow.
        """
        self._logger.warning(f"Alert: {reason}")

    def error(self, cause: Exception) -> None:
        """
        Logs catastrophic failures with stack context.
        """
        self._logger.error(f"Crash inbound: {str(cause)}", exc_info=True)

# Global instance for project-wide chatter
clicker_log: ClickerLogger = ClickerLogger()