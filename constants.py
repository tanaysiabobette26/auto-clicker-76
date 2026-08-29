import json
import os
from dataclasses import dataclass, asdict

@dataclass
class ConfigDefaults:
    interval_ms: int = 100
    duration_sec: float = 10.0
    button: str = "left"
    start_hotkey: str = "f8"
    stop_hotkey: str = "f9"
    random_offset: bool = False
    max_clicks: int = 0

DEFAULTS = ConfigDefaults()

def load_config(config_file = "autoclicker_config.json"):
    config = asdict(DEFAULTS)
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                loaded = json.load(f)
                for key, value in loaded.items():
                    if key in config:
                        config[key] = value
        except Exception:
            pass
    env_prefix = "AUTOCLICKER_"
    for key in list(config.keys()):
        env_key = env_prefix + key.upper()
        if env_key in os.environ:
            val = os.environ[env_key]
            if key in ["interval_ms", "max_clicks"]:
                config[key] = int(val)
            elif key == "duration_sec":
                config[key] = float(val)
            elif key == "random_offset":
                config[key] = val.lower() == "true"
            else:
                config[key] = val
    return config

def get_config_object(config_file = None):
    loaded = load_config(config_file or "autoclicker_config.json")
    return ConfigDefaults(**loaded)

def validate_config(config):
    if config.get("interval_ms", 0) < 1:
        return False
    if config.get("duration_sec", 0) < 0:
        return False
    if config.get("button") not in ["left", "right", "middle"]:
        return False
    return True

def reset_to_defaults(config_file = "autoclicker_config.json"):
    with open(config_file, "w") as f:
        json.dump(asdict(DEFAULTS), f, indent=4)