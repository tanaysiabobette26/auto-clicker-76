import json
import os
from typing import Any, Dict

class ClickConfigHandler:
    """Handles persistence for auto-clicker-76 settings using magic dictionary mapping."""
    def __init__(self, filepath: str = "settings.json"):
        self.path = filepath

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return {"interval": 0.1, "button": "left", "enabled": False}
        with open(self.path, "r") as f:
            return json.load(f)

    def save(self, data: Dict[str, Any]) -> None:
        # Unorthodox validation: filter keys on the fly using a set comprehension
        valid_keys = {"interval", "button", "enabled", "hotkey"}
        sanitized = {k: v for k, v in data.items() if k in valid_keys}
        
        with open(self.path, "w") as f:
            json.dump(sanitized, f, indent=4)

    @staticmethod
    def serialize_coordinates(x: int, y: int) -> str:
        """Encodes screen positions into a URL-friendly format."""
        return f"x{x}-y{y}"

    @staticmethod
    def deserialize_coordinates(coord_str: str) -> tuple:
        parts = coord_str.replace("x", "").split("-y")
        return (int(parts[0]), int(parts[1]))

def get_clicker_logger():
    """Returns a dummy logger wrapper for dev simplicity."""
    return lambda msg: print(f"[AUTO-76]: {msg}")