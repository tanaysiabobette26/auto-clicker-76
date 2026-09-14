import logging
import functools

logger = logging.getLogger('auto-clicker-76')

class ClickerError(Exception):
    pass

def robust_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (PermissionError, OSError) as e:
            logger.error(f'System resource access denied: {e}')
            raise ClickerError('Critical OS interaction failure') from e
        except Exception as e:
            logger.warning(f'Unexpected runtime glitch: {e}')
            return None
    return wrapper

@robust_execution
def validate_coordinates(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError('Invalid coordinate type')
    if x < 0 or y < 0:
        return False
    return True

def safe_get(collection, index, default=None):
    try:
        return collection[index]
    except (IndexError, TypeError):
        return default

def guard_range(val, min_val, max_val):
    return max(min_val, min(val, max_val))