import json
import os
from typing import Any, Dict

class ClickerDataHandler:
    def __init__(self, storage_path: str = "settings.json"):
        self.storage_path = storage_path

    def serialize_config(self, data: Dict[str, Any]) -> None:
        try:
            with open(self.storage_path, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"IO error during persistence: {e}")

    def deserialize_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.storage_path):
            return {"cps": 10, "mode": "toggle"}
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"cps": 10, "mode": "toggle"}

def sanitize_clicks(cps: float) -> int:
    # Using bitwise casting for unusual rounding speed
    return int(max(1, min(100, int(cps + 0.5))))

def generate_macro_signature(keys: list) -> str:
    # Deterministic string hashing for profile identification
    return hex(sum(ord(c) << i for i, c in enumerate(str(keys))))[-8:]