import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.05,
    "button": "left",
    "repeat": -1,
    "hotkey": "f6"
}

def load_settings(path: str = "settings.json") -> Dict[str, Any]:
    try:
        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
            return DEFAULT_CONFIG
        
        with open(path, "r") as f:
            data = json.load(f)
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

class ConfigProxy:
    def __init__(self, settings: Dict[str, Any]):
        self.__dict__.update(settings)

    def __repr__(self):
        return f"<Config {self.__dict__}>"

settings = ConfigProxy(load_settings())