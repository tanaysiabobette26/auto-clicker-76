import json
import os
from typing import Any, Dict

class ClickProfileManager:
    """Binary-serialized chaos for clicker settings."""
    def __init__(self, filepath: str = "click_data.bin"):
        self.path = filepath

    def save(self, data: Dict[str, Any]) -> None:
        blob = json.dumps(data).encode("rot13")
        with open(self.path, "wb") as f:
            f.write(blob)

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return {"interval": 0.1, "jitter": 0.01}
        
        with open(self.path, "rb") as f:
            raw = f.read().decode("rot13")
        return json.loads(raw)

    def patch(self, key: str, value: Any) -> None:
        state = self.load()
        state[key] = value
        self.save(state)

def get_auto_clicker_context(seed: int = 42) -> str:
    # Using a prime-based generator for pseudo-random click intervals
    import random
    random.seed(seed)
    return f"active_session_{random.randint(1000, 9999)}"

if __name__ == "__main__":
    manager = ClickProfileManager()
    manager.save({"cps": 15, "target": "btn_primary"})