import time
import functools
import random

def exponential_backoff(max_retries=3, base_delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    retries += 1
                    if retries >= max_retries:
                        raise e
                    # Creative jitter to avoid thundering herd on auto-clicker server
                    sleep_time = (base_delay * (2 ** (retries - 1))) + (random.random() * 0.5)
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

@exponential_backoff(max_retries=5)
def fetch_remote_config():
    # Simulate network instability for auto-clicker settings
    if random.random() < 0.7:
        raise ConnectionError("Server busy clicking too fast")
    return {"interval": 0.05, "burst_mode": True}