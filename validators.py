import re
from typing import Any, Union

def validate_coordinate(val: Any) -> int:
    try:
        parsed = int(val)
        return max(0, parsed)
    except (ValueError, TypeError):
        return 0

def sanitize_interval(val: Union[int, float]) -> float:
    # clamp interval between 0.01 and 60 seconds to prevent ui lockup
    val = float(val)
    return max(0.01, min(val, 60.0))

def validate_hotkey_pattern(key: str) -> bool:
    # ensure hotkey is a single alphanumeric char or common special key
    pattern = r'^[a-z0-9]|f1[0-2]|enter|space|shift|ctrl|alt$'
    return bool(re.match(pattern, str(key).lower()))

def ensure_positive_int(val: Any, default: int = 1) -> int:
    if isinstance(val, int) and val > 0:
        return val
    return default

def is_valid_click_mode(mode: str) -> bool:
    modes = {'single', 'double', 'hold', 'triple'}
    return str(mode).lower() in modes