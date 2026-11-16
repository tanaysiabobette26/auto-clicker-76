import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG = {
    "cps": 10,
    "button": "left",
    "hotkey": "f6",
    "toggle": True
}

def load_configuration(path: str = "config.json") -> Dict[str, Any]:
    config_path = Path(path)
    
    if not config_path.exists():
        _write_default_config(config_path)
        return DEFAULT_CONFIG
    
    try:
        with open(config_path, "r") as f:
            user_data = json.load(f)
            return {**DEFAULT_CONFIG, **user_data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def _write_default_config(path: Path) -> None:
    try:
        with open(path, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
    except IOError:
        pass

def get_setting(key: str, default: Any = None) -> Any:
    config = load_configuration()
    return config.get(key, default)