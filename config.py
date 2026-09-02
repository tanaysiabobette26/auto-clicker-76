import json
import os
from typing import Dict, Any, Optional

class ConfigLoader:
    def __init__(self, path: Optional[str] = None):
        self.defaults: Dict[str, Any] = {
            "click_interval_ms": 100,
            "click_count": 0,
            "start_hotkey": "f8",
            "stop_hotkey": "f9",
            "mouse_button": "left",
            "randomize_interval": False,
            "random_range": 20,
            "fixed_position": False,
            "pos_x": 0,
            "pos_y": 0
        }
        self.path = path or "auto_clicker_config.json"
        self.config: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        config = self.defaults.copy()
        if os.path.isfile(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                for k, v in loaded.items():
                    if k in config and type(v) == type(config[k]):
                        config[k] = v
            except (json.JSONDecodeError, OSError, TypeError):
                pass
        return config

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.config.get(key, default if default is not None else self.defaults.get(key))

    def __getattr__(self, item: str) -> Any:
        if item in self.config:
            return self.config[item]
        if item in self.defaults:
            return self.defaults[item]
        raise AttributeError(f"'ConfigLoader' object has no attribute '{item}'")

    def update(self, **kwargs: Any) -> None:
        for k, v in kwargs.items():
            if k in self.config:
                self.config[k] = v

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)