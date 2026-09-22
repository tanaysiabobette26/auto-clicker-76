class AutoClickerError(Exception):
    """Base exception for auto-clicker-76 operations."""

class CoordinateOutOfBoundsError(AutoClickerError):
    """Raised when click target is off-screen."""

class ProcessInjectionError(AutoClickerError):
    """Raised when input simulation fails."""

class ConfigValidationError(AutoClickerError):
    """Raised when user configuration is invalid."""

class RateLimitExceededError(AutoClickerError):
    """Raised when clicking frequency exceeds safety limits."""

def raise_if_out_of_bounds(x: int, y: int, screen_dims: tuple[int, int]) -> None:
    width, height = screen_dims
    if not (0 <= x <= width and 0 <= y <= height):
        raise CoordinateOutOfBoundsError(f"Target ({x}, {y}) outside ({width}, {height})")

def validate_interval(ms: int) -> None:
    if ms < 10:
        raise RateLimitExceededError(f"Safety block: {ms}ms is too fast")

def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except AutoClickerError as e:
        print(f"Caught expected simulation error: {e}")
        raise