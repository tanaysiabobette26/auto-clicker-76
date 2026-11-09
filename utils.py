import time
import functools
import random
import logging

logger = logging.getLogger('auto-clicker-76')

def persistent_request(retries=3, backoff=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= retries:
                        logger.error(f'operation failed after {retries} attempts: {e}')
                        raise
                    wait = backoff * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
                    logger.warning(f'attempt {attempts} failed, retrying in {wait:.2f}s...')
                    time.sleep(wait)
        return wrapper
    return decorator

@persistent_request(retries=5)
def fetch_remote_config(url):
    # Simulate network instability for auto-clicker updates
    if random.random() < 0.7:
        raise ConnectionError('server unresponsive')
    return {'click_speed': 100, 'enabled': True}