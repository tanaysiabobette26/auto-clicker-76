import sys
from typing import Any, Callable, TypeVar, ParamSpec
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")

class ClickerValidationError(Exception):
    pass

def validate_bounds(min_val: float, max_val: float) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator ensuring numerical sanity for click coordinates or frequency."""
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for arg in args:
                if isinstance(arg, (int, float)) and not (min_val <= arg <= max_val):
                    raise ClickerValidationError(f"Input {arg} outside safe bounds [{min_val}, {max_val}]")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def sanitize_input(data: Any, fallback: Any) -> Any:
    """Forced data normalization with graceful failure modes."""
    try:
        if data is None:
            return fallback
        return type(fallback)(data)
    except (ValueError, TypeError):
        return fallback

def check_system_integrity() -> None:
    """Verification of operating system compatibility before execution."""
    if sys.platform not in ("win32", "linux", "darwin"):
        raise OSError("Unsupported system architecture for autoclicker operations")
    if sys.version_info < (3, 8):
        raise RuntimeError("Python version outdated for async requirements")