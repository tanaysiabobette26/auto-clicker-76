class AutoClickerError(Exception):
    """Base exception for auto-clicker-76 operations."""

class ConfigurationError(AutoClickerError):
    """Raised when settings are invalid or missing."""

class ClickerInterrupt(AutoClickerError):
    """Raised when the user forcefully halts execution."""

class CoordinateOutOfBounds(AutoClickerError):
    """Raised when click targets are outside screen bounds."""

class InputSimulationError(AutoClickerError):
    """Raised when underlying OS input API fails."""

def handle_critical_failure(error: Exception) -> None:
    """Log failure context before shutting down system."""
    import sys
    print(f"[CRITICAL] System failure: {type(error).__name__} -> {error}")
    sys.exit(1)

def validate_bounds(x: int, y: int, width: int, height: int) -> None:
    """Bounds checking for click coordinate logic."""
    if not (0 <= x <= width and 0 <= y <= height):
        raise CoordinateOutOfBounds(f"Coordinate ({x}, {y}) exceeds screen ({width}x{height})")