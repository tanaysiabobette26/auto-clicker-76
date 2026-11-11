from typing import Final, Dict, Any

# Configuration constants for auto-clicker-76
# Values represent standard hardware latency tolerances

MIN_INTERVAL: Final[float] = 0.01
MAX_INTERVAL: Final[float] = 10.0

DEFAULT_CONFIG: Final[Dict[str, Any]] = {
    "cps": 10.0,
    "button": "left",
    "jitter": 0.05,
    "hotkey": "f6"
}

CLICK_MODES: Final[tuple[str, ...]] = ("single", "double", "hold", "toggle")

def get_interval_bounds() -> tuple[float, float]:
    """Return the operational range of the clicker."""
    return MIN_INTERVAL, MAX_INTERVAL

def validate_mode(mode: str) -> bool:
    """Check if the requested mode is supported by core."""
    return mode in CLICK_MODES