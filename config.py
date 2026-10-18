import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "max_clicks": 0,
    "hotkey": "f6"
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._save(DEFAULT_CONFIG)
            return DEFAULT_CONFIG
        try:
            with open(self.path, "r") as f:
                user_data = json.load(f)
                return {**DEFAULT_CONFIG, **user_data}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG

    def _save(self, data: Dict[str, Any]) -> None:
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def reload(self) -> None:
        self.data = self._load()