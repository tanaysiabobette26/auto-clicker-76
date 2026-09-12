import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": -1,
    "hotkey": "f6"
}

class ConfigManager:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
                return {**DEFAULT_CONFIG, **loaded}
        except (FileNotFoundError, json.JSONDecodeError):
            self._save_defaults()
            return DEFAULT_CONFIG

    def _save_defaults(self):
        with open(self.path, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)

    def get(self, key: str) -> Any:
        return self.data.get(key, DEFAULT_CONFIG.get(key))

    def update(self, key: str, value: Any):
        self.data[key] = value
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

config_instance = ConfigManager()