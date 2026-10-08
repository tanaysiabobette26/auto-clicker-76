from typing import Final, Dict, Any

# Configuration constants for auto-clicker-76 movement and timing
MIN_INTERVAL: Final[float] = 0.01
MAX_INTERVAL: Final[float] = 10.0

# Standard screen coordinate mapping for event handling
SCREEN_BOUNDARIES: Final[Dict[str, int]] = {
    'min_x': 0,
    'min_y': 0,
    'max_x': 1920,
    'max_y': 1080
}

# Dynamic key mapping for click trigger execution
TRIGGER_MAP: Final[Dict[str, str]] = {
    'start': 'f6',
    'stop': 'f7',
    'emergency_exit': 'esc'
}

def get_default_config() -> Dict[str, Any]:
    """Returns the initial operational state configuration."""
    return {
        'interval': 0.1,
        'button': 'left',
        'iterations': -1,
        'jitter': True
    }

# Session logging verbosity levels
LOG_LEVELS: Final[Dict[int, str]] = {
    0: 'DEBUG',
    1: 'INFO',
    2: 'WARNING',
    3: 'CRITICAL'
}