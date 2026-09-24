import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('auto-clicker-76')

def retry_operation(attempts=3, delay=1.0, backoff=2):
    """Decorator applying exponential backoff for network stability."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tries, current_delay = attempts, delay
            while tries > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries -= 1
                    if tries == 0:
                        logger.error(f'operation failed after {attempts} attempts: {e}')
                        raise
                    logger.warning(f'attempt failed, retrying in {current_delay}s... ({tries} left)')
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(attempts=3)
def ping_server(url):
    """Example network probe for clicker registration."""
    import random
    if random.random() < 0.7:
        raise ConnectionError('flickering network ghost')
    return True