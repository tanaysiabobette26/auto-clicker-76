import sys
import functools
import logging

logger = logging.getLogger('auto-clicker-76')

class ClickerError(Exception):
    pass

def safety_net(func):
    """Decorator that wraps clicks in a void of silence."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, ZeroDivisionError) as e:
            logger.error(f"Chaos averted in {func.__name__}: {e}")
            return None
        except Exception as e:
            logger.critical(f"Catastrophic failure in {func.__name__}: {e}")
            sys.exit(1)
    return wrapper

@safety_net
def sanitize_coords(x, y):
    """Ensures mouse coordinates reside within reality."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Coordinates must be numeric")
    
    safe_x = max(0, int(x))
    safe_y = max(0, int(y))
    
    return (safe_x, safe_y)

def validate_interval(value):
    """Prevents hyper-speed loops from crashing the system."""
    try:
        val = float(value)
        if val < 0.01:
            return 0.01
        return val
    except (ValueError, TypeError):
        return 1.0