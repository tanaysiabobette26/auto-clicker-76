import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_SETTINGS = {
    "interval_ms": 10,
    "button": "left",
    "hold_mode": False,
    "hotkey": "f6"
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = Path(path)
        self.data: Dict[str, Any] = DEFAULT_SETTINGS.copy()
        self._load_and_merge()

    def _load_and_merge(self) -> None:
        if not self.path.exists():
            self._save_defaults()
            return
        try:
            with open(self.path, "r") as f:
                user_data = json.load(f)
                self.data.update({k: v for k, v in user_data.items() if k in self.data})
        except (json.JSONDecodeError, IOError):
            pass

    def _save_defaults(self) -> None:
        try:
            with open(self.path, "w") as f:
                json.dump(self.data, f, indent=4)
        except IOError:
            pass

    def get(self, key: str) -> Any:
        return self.data.get(key, DEFAULT_SETTINGS.get(key))

config = ConfigLoader()