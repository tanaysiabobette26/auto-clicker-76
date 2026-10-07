import logging
import functools
import time

logger = logging.getLogger('auto-clicker-76')

class ClickerError(Exception):
    pass

def robust_click(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            try:
                return func(*args, **kwargs)
            except (PermissionError, OSError) as e:
                attempts += 1
                logger.warning(f'click event failed, retry {attempts}/{max_attempts}: {e}')
                time.sleep(0.5 * attempts)
        raise ClickerError(f'critical failure after {max_attempts} attempts')
    return wrapper

def validate_coordinates(x, y):
    try:
        x, y = int(x), int(y)
        if x < 0 or y < 0:
            raise ValueError('negative coordinates')
        return x, y
    except (ValueError, TypeError) as e:
        logger.error(f'invalid coordinate mapping: {e}')
        return 0, 0

def safe_execute(task_fn, *args):
    try:
        return task_fn(*args)
    except Exception as e:
        logger.critical(f'unhandled execution error: {e}')
        return None