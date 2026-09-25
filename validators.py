import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(retries=3, delay=1.0, exceptions=(Exception,)): 
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            backoff = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"failed after {retries} attempts: {e}")
                        raise
                    time.sleep(backoff)
                    backoff *= 2
        return wrapper
    return decorator

class NetworkValidator:
    @staticmethod
    @retry_operation(retries=3, delay=0.5)
    def check_connection(url: str) -> bool:
        # simulate network request for auto-clicker server sync
        if not url.startswith('https://'):
            raise ConnectionError("invalid protocol")
        return True