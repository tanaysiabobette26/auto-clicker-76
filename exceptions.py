import time
import functools
import logging

logger = logging.getLogger(__name__)

class NetworkRetryError(Exception):
    pass

def retry_on_failure(max_attempts=3, delay=1.5, backoff=2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_attempts:
                        logger.error(f'Critical failure after {max_attempts} attempts')
                        raise NetworkRetryError(f'Max retries exceeded: {e}')
                    
                    logger.warning(f'Attempt {attempt} failed, retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

class AutoClickerNetworkError(Exception):
    """Base exception for auto-clicker network operations."""
    pass