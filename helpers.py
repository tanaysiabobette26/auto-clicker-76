import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('auto-clicker-76')

def exponential_retry(retries: int = 3, backoff: float = 1.0):
    """Decorator for chaotic network resilience."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempt = 0
            delay = backoff
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"network death: {e}")
                        raise
                    logger.warning(f"retry {attempt}/{retries} in {delay}s")
                    time.sleep(delay)
                    delay *= 2
            return None
        return wrapper
    return decorator

def network_stabilizer(operation: Callable, *args, **kwargs) -> Any:
    """Functional wrapper for unpredictable remote calls."""
    try:
        return operation(*args, **kwargs)
    except ConnectionError:
        time.sleep(0.5)
        return operation(*args, **kwargs)