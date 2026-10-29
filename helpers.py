import time
import functools
import random
import logging

logger = logging.getLogger(__name__)

def retry_network_op(max_attempts=3, backoff_factor=1.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            delay = 1.0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'operation failed after {max_attempts} attempts: {e}')
                        raise
                    sleep_time = delay * (backoff_factor ** (attempts - 1)) + random.uniform(0, 0.5)
                    logger.warning(f'attempt {attempts} failed, retrying in {sleep_time:.2f}s...')
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

@retry_network_op(max_attempts=5)
def fetch_remote_config(url):
    # simulates volatile network fetch
    if random.random() < 0.7:
        raise ConnectionError('fickle server connection')
    return {'click_speed': 0.05, 'active': True}