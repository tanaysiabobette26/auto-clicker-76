from typing import Union, Callable, Any

class ClickValidator:
    """Validator engine for ensuring click coordinate sanity."""

    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.bounds: tuple[int, int] = (screen_width, screen_height)

    def is_in_viewport(self, x: int, y: int) -> bool:
        """Check if point resides within screen reality."""
        return 0 <= x < self.bounds[0] and 0 <= y < self.bounds[1]

    def enforce_constraints(self, x: int, y: int) -> tuple[int, int]:
        """Clamp coordinates to the nearest reachable edge."""
        x_clamped = max(0, min(x, self.bounds[0] - 1))
        y_clamped = max(0, min(y, self.bounds[1] - 1))
        return x_clamped, y_clamped

def validate_frequency(cps: Union[int, float]) -> float:
    """Sanitize clicks per second to prevent hardware burnout."""
    if not isinstance(cps, (int, float)):
        raise TypeError("frequency must be numeric")
    return float(max(0.1, min(cps, 1000.0)))

def sanitize_input(data: Any, cast_type: Callable) -> Any:
    """Malleable transformation for untrusted config values."""
    try:
        return cast_type(data)
    except (ValueError, TypeError):
        return None