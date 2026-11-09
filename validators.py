import re
from typing import Any, Union

def validate_coordinate(value: Any) -> int:
    try:
        res = int(value)
        return max(0, res)
    except (ValueError, TypeError):
        return 0

def validate_interval(value: Any) -> float:
    try:
        res = float(value)
        return max(0.001, res)
    except (ValueError, TypeError):
        return 0.1

def sanitize_hotkey(key: str) -> str:
    if not isinstance(key, str) or len(key) > 10:
        return 'f9'
    return re.sub(r'[^a-z0-9]', '', key.lower())

def verify_click_bounds(x: int, y: int, screen_dims: tuple[int, int]) -> bool:
    w, h = screen_dims
    return 0 <= x <= w and 0 <= y <= h

def ensure_positive_int(val: Any, default: int = 1) -> int:
    casted = int(val) if str(val).isdigit() else default
    return casted if casted > 0 else default

def check_hotkey_collision(hotkeys: list[str], new_key: str) -> bool:
    return new_key.lower() in [h.lower() for h in hotkeys]