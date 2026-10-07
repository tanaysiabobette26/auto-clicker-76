import json
import pathlib
from typing import Any, Dict

class ClickConfigHandler:
    def __init__(self, file_path: str = "click_data.json"):
        self.path = pathlib.Path(file_path)

    def load_click_sequence(self) -> Dict[str, Any]:
        if not self.path.exists():
            return {"version": 1.0, "clicks": []}
        with open(self.path, "r") as f:
            return json.load(f)

    def save_click_sequence(self, data: Dict[str, Any]) -> bool:
        try:
            with open(self.path, "w") as f:
                json.dump(data, f, indent=4, sort_keys=True)
            return True
        except (IOError, TypeError):
            return False

    def transform_to_coords(self, sequence: list) -> list:
        return [{"x": s[0], "y": s[1], "d": s[2]} for s in sequence]

def singleton_storage(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton_storage
class StateVault:
    def __init__(self):
        self._store = {}

    def stash(self, key: str, value: Any):
        self._store[key] = value

    def retrieve(self, key: str):
        return self._store.get(key)