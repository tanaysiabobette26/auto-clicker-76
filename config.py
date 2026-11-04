import json
import os
from collections import ChainMap
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "cps": 12.5,
    "button": "left",
    "hotkey": "<ctrl>+<alt>+a",
    "random_jitter_ms": 18,
    "burst_mode": False,
    "burst_count": 5,
    "sound_feedback": True,
}


class ConfigProxy:
    """Dynamic configuration wrapper with type safety and fallback chains."""

    def __init__(self, config_path: str = "clicker_config.json"):
        self._path = config_path
        self._file_data = self._load_file()
        self._env_data = self._load_env()
        self._store = ChainMap(self._env_data, self._file_data, DEFAULT_CONFIG)

    def _load_file(self) -> Dict[str, Any]:
        if os.path.exists(self._path):
            try:
                with open(self._path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
        return {}

    def _load_env(self) -> Dict[str, Any]:
        env_map = {}
        prefix = "AUTOCLICKER_"
        for key, default_val in DEFAULT_CONFIG.items():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                raw = os.environ[env_key]
                target_type = type(default_val)
                try:
                    if target_type is bool:
                        env_map[key] = raw.lower() in ("1", "true", "yes")
                    else:
                        env_map[key] = target_type(raw)
                except ValueError:
                    pass
        return env_map

    def __getattr__(self, name: str) -> Any:
        if name in self._store:
            return self._store[name]
        raise AttributeError(f"Configuration key '{name}' not found")

    def __getitem__(self, item: str) -> Any:
        return self._store[item]

    def reload(self) -> None:
        self._file_data = self._load_file()
        self._env_data = self._load_env()
        self._store.maps = [self._env_data, self._file_data, DEFAULT_CONFIG]

    def export(self) -> Dict[str, Any]:
        return dict(self._store)


config = ConfigProxy()
