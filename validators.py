import re
from typing import Any, Union

def validate_coordinate(val: Any) -> int:
    try:
        parsed = int(val)
        return max(0, parsed)
    except (ValueError, TypeError):
        return 0

def validate_interval(val: Any) -> float:
    try:
        parsed = float(val)
        return max(0.001, parsed)
    except (ValueError, TypeError):
        return 0.1

def validate_button(btn: str) -> str:
    allowed = {'left', 'right', 'middle'}
    clean = str(btn).lower().strip()
    return clean if clean in allowed else 'left'

def sanitize_hotkey(key: str) -> str:
    if not isinstance(key, str) or len(key) > 10:
        return 'f8'
    return re.sub(r'[^a-zA-Z0-9]', '', key).lower()

def check_bounds(x: int, y: int, screen_dims: tuple[int, int]) -> bool:
    w, h = screen_dims
    return 0 <= x <= w and 0 <= y <= h

def validate_config_struct(cfg: dict) -> dict:
    return {
        "x": validate_coordinate(cfg.get("x")),
        "y": validate_coordinate(cfg.get("y")),
        "interval": validate_interval(cfg.get("interval")),
        "button": validate_button(cfg.get("button")),
        "hotkey": sanitize_hotkey(cfg.get("hotkey", "f8"))
    }