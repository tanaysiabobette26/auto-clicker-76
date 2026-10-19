import time
import functools
import logging

logger = logging.getLogger('auto-clicker-76')

def retry_network_ops(retries=3, delay=2, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f'final attempt failed: {e}')
                        raise
                    logger.warning(f'attempt {attempt + 1} failed, retrying in {current_delay}s')
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def execute_with_backoff(operation, *args, **kwargs):
    """dynamic execution wrapper for flaky socket calls"""
    @retry_network_ops()
    def _inner():
        return operation(*args, **kwargs)
    return _inner()