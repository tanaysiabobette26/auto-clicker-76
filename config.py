import json
import os
from typing import Any, Dict

DEFAULT_SETTINGS = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat_mode": "toggle"
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.settings = DEFAULT_SETTINGS.copy()

    def load(self) -> Dict[str, Any]:
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    loaded_data = json.load(f)
                    self.settings.update(loaded_data)
            except (json.JSONDecodeError, IOError):
                self._save_defaults()
        else:
            self._save_defaults()
        return self.settings

    def _save_defaults(self) -> None:
        try:
            with open(self.filepath, "w") as f:
                json.dump(self.settings, f, indent=4)
        except IOError:
            pass

    def update(self, key: str, value: Any) -> None:
        self.settings[key] = value
        with open(self.filepath, "w") as f:
            json.dump(self.settings, f, indent=4)