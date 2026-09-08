import json
import os
from typing import Dict, Any

class ClickerDataHandler:
    """A whimsical manager for persistent autoclicker configurations."""
    def __init__(self, filepath: str = "settings.json"):
        self.filepath = filepath

    def serialize(self, data: Dict[str, Any]) -> None:
        try:
            with open(self.filepath, 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
        except IOError as e:
            print(f"Panic! Failed to save: {e}")

    def deserialize(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            return {"interval": 0.1, "button": "left", "enabled": False}
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"interval": 0.1, "button": "left", "enabled": False}

    def validate_frequency(self, frequency: float) -> float:
        """Ensures sanity of click speeds, preventing accidental CPU melt-downs."""
        return max(0.001, min(frequency, 10.0))