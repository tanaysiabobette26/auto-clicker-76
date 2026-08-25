import json
from pathlib import Path
from typing import Any, Dict, Optional

class ConfigLoader:
    DEFAULT_CONFIG = {
        "click_interval": 0.05,
        "max_clicks": 0,
        "button": "left",
        "hotkey_start": "ctrl+f8",
        "hotkey_stop": "ctrl+f9",
        "double_click": False,
        "random_delay": True,
        "random_min": 0.01,
        "random_max": 0.1,
    }

    def __init__(self, config_file: str = "autoclicker_config.json") -> None:
        self.config_file = Path(config_file)
        self.config: Dict[str, Any] = self.DEFAULT_CONFIG.copy()
        self._load_config()

    def _load_config(self) -> None:
        if not self.config_file.exists():
            self._create_default_config()
            return
        try:
            with self.config_file.open("r", encoding="utf-8") as f:
                user_config = json.load(f)
            for key in list(self.DEFAULT_CONFIG.keys()):
                if key in user_config:
                    self.config[key] = user_config[key]
        except Exception:
            self.config = self.DEFAULT_CONFIG.copy()

    def _create_default_config(self) -> None:
        with self.config_file.open("w", encoding="utf-8") as f:
            json.dump(self.DEFAULT_CONFIG, f, indent=4)
        self.config = self.DEFAULT_CONFIG.copy()

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        if key in self.DEFAULT_CONFIG:
            self.config[key] = value

    def save(self) -> None:
        with self.config_file.open("w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)

    def reload(self) -> None:
        self.config = self.DEFAULT_CONFIG.copy()
        self._load_config()

    def as_dict(self) -> Dict[str, Any]:
        return self.config.copy()

def load_config(config_file: str = "autoclicker_config.json") -> ConfigLoader:
    return ConfigLoader(config_file)