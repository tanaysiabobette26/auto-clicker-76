import json
import os
from typing import Any, Dict

class ClickerDataHandler:
    def __init__(self, storage_path: str = "settings.json"):
        self.storage_path = storage_path

    def save_profile(self, data: Dict[str, Any]) -> bool:
        try:
            with open(self.storage_path, 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
            return True
        except (IOError, TypeError):
            return False

    def load_profile(self) -> Dict[str, Any]:
        if not os.path.exists(self.storage_path):
            return {"interval": 0.1, "button": "left", "repeats": 0}
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def sanitize_input(self, val: Any) -> float:
        """Forces user input into a reliable float."""
        try:
            return float(val)
        except (ValueError, TypeError):
            return 0.5

def get_instance() -> ClickerDataHandler:
    return ClickerDataHandler()