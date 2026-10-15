import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_SETTINGS = {
    "interval": 0.01,
    "button": "left",
    "hotkey": "f6",
    "repeat": -1,
    "jitter": 0.005
}

class ConfigManager:
    def __init__(self, path: str = "settings.json"):
        self.path = Path(path)
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.path.exists():
            self._save(DEFAULT_SETTINGS)
            return DEFAULT_SETTINGS
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
                return {**DEFAULT_SETTINGS, **loaded}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_SETTINGS

    def _save(self, data: Dict[str, Any]) -> None:
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name, DEFAULT_SETTINGS.get(name))

config = ConfigManager()