import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

class ConfigLoader:
    def __init__(self, path: str = "settings.json"):
        self.path = path

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self._save_defaults()
        try:
            with open(self.path, "r") as f:
                user_config = json.load(f)
                return {**DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    def _save_defaults(self) -> Dict[str, Any]:
        try:
            with open(self.path, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except IOError:
            pass
        return DEFAULT_CONFIG.copy()

config = ConfigLoader().load()