import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.json'):
        self.path = path
        self.defaults = {
            'interval': 0.01,
            'button': 'left',
            'hotkey': 'f8',
            'random_jitter': True
        }

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._write_defaults()
            return self.defaults
        try:
            with open(self.path, 'r') as f:
                data = json.load(f)
                return {**self.defaults, **data}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def _write_defaults(self) -> None:
        try:
            with open(self.path, 'w') as f:
                json.dump(self.defaults, f, indent=4)
        except IOError:
            pass

class AutoclickerConfig:
    def __init__(self):
        self._data = ConfigLoader().load()

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name)

    def __repr__(self) -> str:
        return f"AutoclickerConfig({self._data})"