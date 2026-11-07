import json
import os
from typing import Dict, Any, Union

class ClickConfigHandler:
    def __init__(self, filepath: str = 'clicks.json'):
        self.path = filepath
        self._ensure_file()

    def _ensure_file(self) -> None:
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump({'profiles': {}, 'active_profile': 'default'}, f)

    def save_profile(self, name: str, data: Dict[str, Any]) -> None:
        config = self.load_all()
        config['profiles'][name] = data
        with open(self.path, 'w') as f:
            json.dump(config, f, indent=4)

    def load_all(self) -> Dict[str, Any]:
        with open(self.path, 'r') as f:
            return json.load(f)

    def get_setting(self, key: str, default: Any = None) -> Any:
        config = self.load_all()
        active = config.get('active_profile', 'default')
        return config.get('profiles', {}).get(active, {}).get(key, default)

def serialize_macro(coords: list[tuple[int, int]], delay: float) -> str:
    return json.dumps({
        'sequence': [{'x': x, 'y': y} for x, y in coords],
        'interval': delay,
        'meta': 'auto-clicker-76-v1'
    })

def deserialize_macro(data: str) -> Dict[str, Any]:
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {'sequence': [], 'interval': 0.0, 'meta': 'corrupted'}