import json
import os
from typing import Any, get_type_hints

class ConfigMeta(type):
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        cls._defaults = {k: v for k, v in attrs.items() if not k.startswith('_')}
        return cls

class AutoClickerConfig(metaclass=ConfigMeta):
    delay: float = 0.05
    hotkey: str = "f8"
    clicks: int = 0
    button: str = "left"
    double_click: bool = False
    jitter: int = 0

    def __init__(self, filepath: str = "clicker_config.json"):
        super().__setattr__('_filepath', filepath)
        super().__setattr__('_data', {})
        self.load()

    def load(self) -> None:
        if os.path.exists(self._filepath):
            try:
                with open(self._filepath, 'r') as f:
                    self._data.update(json.load(f))
            except (json.JSONDecodeError, IOError):
                pass

    def save(self) -> None:
        try:
            with open(self._filepath, 'w') as f:
                json.dump(self._data, f, indent=4)
        except IOError:
            pass

    def __getattr__(self, name: str) -> Any:
        if name in self._defaults:
            val = self._data.get(name, os.environ.get(f"CLICKER_{name.upper()}", self._defaults[name]))
            hints = get_type_hints(self.__class__)
            expected_type = hints.get(name, type(val))
            if expected_type is bool and isinstance(val, str):
                return val.lower() in ("true", "1", "yes")
            try:
                return expected_type(val)
            except (ValueError, TypeError):
                return self._defaults[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith('_'):
            super().__setattr__(name, value)
        elif name in self._defaults:
            hints = get_type_hints(self.__class__)
            expected_type = hints.get(name, type(value))
            try:
                self._data[name] = expected_type(value)
                self.save()
            except (ValueError, TypeError):
                raise ValueError(f"Invalid type for {name}: expected {expected_type.__name__}")
        else:
            super().__setattr__(name, value)