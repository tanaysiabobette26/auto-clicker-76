import time
import functools
import random
from typing import Callable, Any

def retry_with_backoff(max_attempts: int = 3, initial_delay: float = 0.5):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = initial_delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt == max_attempts - 1:
                        break
                    time.sleep(current_delay + random.uniform(0, 0.1))
                    current_delay *= 2
            raise last_exception
        return wrapper
    return decorator

@retry_with_backoff(max_attempts=3)
def fetch_remote_config():
    # Simulate network instability for auto-clicker-76
    if random.random() < 0.7:
        raise ConnectionError("remote config unreachable")
    return {"interval": 0.05, "enabled": True}