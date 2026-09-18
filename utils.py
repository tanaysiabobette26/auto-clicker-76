import time
import random
import functools
from typing import Callable, Any

class NetworkException(Exception):
    pass

def retry_with_jitter(retries: int = 3, base_delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_ex = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 0.1)
                    time.sleep(delay)
            raise NetworkException(f'failed after {retries} attempts: {last_ex}')
        return wrapper
    return decorator

@retry_with_jitter(retries=3, base_delay=0.5)
def ping_server(url: str):
    # Simulate volatile network state
    if random.random() < 0.7:
        raise ConnectionError('fickle server')
    return True