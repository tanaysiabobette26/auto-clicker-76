import json
import os

DEFAULT_CONFIG = {
    "cps": 15,
    "hotkey": "F6",
    "hold_mode": False,
    "randomization_ms": 12,
    "jitter_pixels": 2
}

class AutoClickerConfig(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"Config missing key: {key}")

    def __setattr__(self, key, value):
        self[key] = value

def load_config(filepath="config.json") -> AutoClickerConfig:
    config = DEFAULT_CONFIG.copy()
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                user_data = json.load(f)
                config.update({k: v for k, v in user_data.items() if k in config})
        except Exception:
            pass
    return AutoClickerConfig(config)

active_config = load_config()