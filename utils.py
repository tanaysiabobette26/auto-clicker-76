import logging
import functools

logger = logging.getLogger('auto-clicker-76')

class ClickerError(Exception):
    """Base exception for auto-clicker operations."""
    pass

def robust_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (PermissionError, OSError) as e:
            logger.error(f'Critical hardware interaction failure: {e}')
            raise ClickerError('Input device is currently inaccessible.') from e
        except Exception as e:
            logger.warning(f'Unexpected jitter during operation: {e}')
            return None
    return wrapper

def validate_coordinates(x: int, y: int):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('Pixel coordinates must be integers')
    if x < 0 or y < 0:
        raise ValueError('Screen bounds violation detected')
    return True

def safe_click_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            validate_coordinates(args[0], args[1])
            return func(*args, **kwargs)
        except (ValueError, IndexError) as e:
            logger.error(f'Coordinate validation failure: {e}')
            return False
    return wrapper