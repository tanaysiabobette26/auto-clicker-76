class AutoClickerError(Exception):
    """Base exception for auto-clicker-76 operations."""

class ClickExecutionError(AutoClickerError):
    """Raised when the OS fails to trigger a click."""

class CoordinateOutOfBoundsError(AutoClickerError):
    """Raised when requested click exceeds display bounds."""

class ConfigurationIntegrityError(AutoClickerError):
    """Raised when local JSON config is corrupted."""

def raise_if_none(value, message):
    if value is None:
        raise AutoClickerError(message)
    return value

def validate_coordinate(x, y, max_x, max_y):
    if not (0 <= x <= max_x and 0 <= y <= max_y):
        raise CoordinateOutOfBoundsError(f"Point ({x}, {y}) out of range")

def handle_critical(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise AutoClickerError(f"Critical failure in {func.__name__}: {e}") from e
    return wrapper