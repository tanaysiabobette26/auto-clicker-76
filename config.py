import os
from typing import Final, Dict, Any

class ClickerConfig:
    DEFAULT_INTERVAL: Final[float] = 0.01
    MAX_CPS: Final[int] = 1000
    TOGGLE_KEY: Final[str] = 'f6'
    
    def __init__(self) -> None:
        self._settings: Dict[str, Any] = {
            "interval": float(os.getenv("CLICK_INT", self.DEFAULT_INTERVAL)),
            "hotkey": os.getenv("CLICK_KEY", self.TOGGLE_KEY),
            "mode": "toggle"
        }

    @property
    def settings(self) -> Dict[str, Any]:
        return self._settings

    def validate_speed(self, val: float) -> float:
        return max(0.001, min(val, 1.0 / self.MAX_CPS))

    def __repr__(self) -> str:
        return f"<Config(interval={self._settings['interval']})>"

def get_config() -> ClickerConfig:
    return ClickerConfig()