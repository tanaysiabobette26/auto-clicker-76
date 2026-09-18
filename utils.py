import sys
import time
import functools
from typing import Callable, Any

class ClickerError(Exception):
    """Custom escalation for volatile input handling."""
    pass

def safety_net(max_retries: int = 3, delay: float = 0.5):
    """Decorator for resilience against sporadic hardware interrupts."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (OSError, RuntimeError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        raise ClickerError(f"Hardware unreachable: {e}")
                    time.sleep(delay * attempts)
            return None
        return wrapper
    return decorator

def validate_coordinates(x: int, y: int) -> bool:
    """Boundary verification for viewport constraints."""
    try:
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError("Non-integer coordinate sequence")
        return True
    except ValueError:
        return False

def emergency_abort(reason: str):
    """Instant process termination for critical failures."""
    sys.stderr.write(f"[CRITICAL] {reason}\n")
    sys.exit(1)