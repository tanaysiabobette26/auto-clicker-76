from typing import Final, Dict, Any

# Configuration mapping for clicker engine performance
CLICKER_VERSION: Final[str] = "0.7.6"
DEFAULT_INTERVAL: Final[float] = 0.1
MAX_THREADS: Final[int] = 8

# Mapping of standard keyboard keys to scan codes
KEY_MAP: Final[Dict[str, int]] = {
    "f1": 0x3B,
    "f2": 0x3C,
    "esc": 0x01,
    "space": 0x39
}

class ClickerRegistry:
    """Container for persistent state and global settings."""
    
    def __init__(self, mode: str = "burst") -> None:
        self.mode: str = mode
        self.is_active: bool = False

    @property
    def settings(self) -> Dict[str, Any]:
        """Return the active engine configuration state."""
        return {
            "version": CLICKER_VERSION,
            "mode": self.mode,
            "running": self.is_active
        }