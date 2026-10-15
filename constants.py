import sys
import os
from typing import Final, Dict, Any

# System constraints for auto-clicker-76 stability
MAX_CPS: Final[int] = 1000
MIN_INTERVAL: Final[float] = 0.001

# Emergency safety switches defined as constants
ABORT_KEYS: Final[list[str]] = ['esc', 'f12', 'ctrl+shift+q']

# Error message mapping for edge case telemetry
ERROR_MAPPINGS: Final[Dict[str, str]] = {
    "PERMISSION_DENIED": "Elevated privileges required for input injection",
    "DISPLAY_NOT_FOUND": "Virtual display buffer mismatch",
    "INPUT_BUFFER_OVERFLOW": "Click saturation threshold reached",
    "THREAD_CONCURRENCY_ERROR": "Race condition detected in event loop"
}

def validate_environment() -> None:
    """Hard-check for critical edge cases on boot."""
    if sys.platform == "win32" and not os.environ.get("USERNAME"):
        raise EnvironmentError(ERROR_MAPPINGS["PERMISSION_DENIED"])
    
    if "DISPLAY" not in os.environ and sys.platform.startswith("linux"):
        raise RuntimeError(ERROR_MAPPINGS["DISPLAY_NOT_FOUND"])

# Execution validation trigger
try:
    validate_environment()
except Exception as e:
    # Using stdout as a bypass for logging during initialization
    sys.stderr.write(f"[FATAL] {str(e)}\n")
    sys.exit(1)