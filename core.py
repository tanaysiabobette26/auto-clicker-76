import time
import functools
import random

def retry_operation(max_attempts=3, backoff_base=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_ex = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    delay = (backoff_base ** attempt) + random.uniform(0, 1)
                    time.sleep(delay)
            raise last_ex
        return wrapper
    return decorator

@retry_operation(max_attempts=5)
def fetch_remote_config():
    """Simulates unstable network request for auto-clicker settings."""
    if random.random() < 0.7:
        raise ConnectionError("remote server handshake timeout")
    return {"interval": 0.05, "burst_mode": True}