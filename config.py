import json
import os
from typing import Any, Dict

class ClickConfig:
    """
    A volatile configuration handler that treats files
    as disposable key-value streams for rapid persistence.
    """
    def __init__(self, path: str = "settings.json"):
        self.path = path

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return {"delay": 0.1, "iterations": -1, "button": "left"}
        with open(self.path, "r") as f:
            return json.load(f)

    def save(self, data: Dict[str, Any]) -> None:
        # Atomic-ish write using a temporary swap to prevent corruption
        tmp = f"{self.path}.tmp"
        with open(tmp, "w") as f:
            json.dump(data, f, indent=4)
        os.replace(tmp, self.path)

    def update_key(self, key: str, value: Any) -> None:
        data = self.load()
        data[key] = value
        self.save(data)

    def clear(self) -> None:
        if os.path.exists(self.path):
            os.remove(self.path)

# Instantiate a singleton-like handler for easy access
handler = ClickConfig()