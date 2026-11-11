import json
import os
from pathlib import Path

DEFAULT_CONFIG = {
    "cps": 10,
    "button": "left",
    "toggle_key": "f6",
    "anti_detect": True
}

class ConfigManager:
    def __init__(self, path="config.json"):
        self.path = Path(path)
        self.settings = self._load()

    def _load(self):
        if not self.path.exists():
            return self._save_defaults()
        try:
            with open(self.path, "r") as f:
                return {**DEFAULT_CONFIG, **json.load(f)}
        except (json.JSONDecodeError, IOError):
            return self._save_defaults()

    def _save_defaults(self):
        with open(self.path, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG

    def get(self, key):
        return self.settings.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self.settings[key] = value
        with open(self.path, "w") as f:
            json.dump(self.settings, f, indent=4)

config = ConfigManager()