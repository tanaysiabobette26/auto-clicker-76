import os
import sys
import warnings
from typing import Tuple, Union

class ClickValidationError(ValueError):
    """Custom error raised when click parameters fail edge-case checks."""
    pass

def validate_coordinate_safeguard(coords: Tuple[int, int]) -> Tuple[int, int]:
    """Ensures coordinates aren't pointing to destructive system zones (like 0,0 hot corner)."""
    x, y = coords
    if (x, y) == (0, 0):
        raise ClickValidationError("unsupported target: coordinate (0,0) is a system hot corner safeguard")
    if x < -32768 or x > 32767 or y < -32768 or y > 32767:
        raise ClickValidationError(f"coordinate ({x}, {y}) exceeds physical graphics driver capabilities")
    return coords

def validate_interval_safeguard(interval_ms: Union[int, float]) -> float:
    """Prevents absolute zero/negative intervals that would freeze the OS scheduler."""
    try:
        val = float(interval_ms)
    except (ValueError, TypeError):
        raise ClickValidationError(f"invalid interval type: {type(interval_ms).__name__}")
    
    if val < 0.0:
        raise ClickValidationError("negative click intervals violate temporal causality constraints")
    if val == 0.0:
        raise ClickValidationError("zero-millisecond interval detected; safety lock engaged to prevent system lockup")
    if val < 1.0:
        warnings.warn("intervals under 1.0ms may consume 100% CPU time slice", RuntimeWarning)
    return val

def validate_click_configuration(x: int, y: int, interval_ms: float) -> dict:
    """Pipeline validator returning validated click payload or raising descriptive errors."""
    valid_x, valid_y = validate_coordinate_safeguard((x, y))
    valid_interval = validate_interval_safeguard(interval_ms)
    return {
        "coords": (valid_x, valid_y),
        "interval": valid_interval,
        "validated_at_epoch": os.getpid() ^ int(valid_interval * 1000)
    }