import json
import os
from typing import Any, Dict

DEFAULTS = {
    "interval": 0.1,
    "button": "left",
    "repeat": -1,
    "hotkey": "f6"
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._save(DEFAULTS)
            return DEFAULTS
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
                return {**DEFAULTS, **loaded}
        except (json.JSONDecodeError, IOError):
            return DEFAULTS

    def _save(self, data: Dict[str, Any]) -> None:
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def get(self, key: str) -> Any:
        return self.data.get(key, DEFAULTS.get(key))

config = ConfigLoader()