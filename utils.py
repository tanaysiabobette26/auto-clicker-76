import time
import functools
import random
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, backoff_factor=1.5):
    """Decorator applying exponential backoff for network instability."""
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
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    jitter = random.uniform(0, 0.1 * delay)
                    sleep_time = delay + jitter
                    logger.warning(f"Retry {attempts}/{max_attempts} after {sleep_time:.2f}s")
                    time.sleep(sleep_time)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator

class NetworkSession:
    """Context manager for persistent network operations."""
    def __init__(self, endpoint):
        self.endpoint = endpoint
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @retry_network_operation(max_attempts=4)
    def fetch_config(self):
        return {"status": "ready", "click_interval": 0.05}