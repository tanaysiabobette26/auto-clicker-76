import json
import os
from typing import Any, Dict

class ConfigLoader:
    DEFAULT_CONFIG = {
        "interval": 0.1,
        "button": "left",
        "jitter": False,
        "max_clicks": 1000
    }

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            self._write_defaults()
            return self.DEFAULT_CONFIG
        
        try:
            with open(self.filepath, 'r') as f:
                user_config = json.load(f)
                return {**self.DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_CONFIG

    def _write_defaults(self) -> None:
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.DEFAULT_CONFIG, f, indent=4)
        except IOError:
            pass

def get_config(path: str = "config.json") -> Dict[str, Any]:
    loader = ConfigLoader(path)
    return loader.load()