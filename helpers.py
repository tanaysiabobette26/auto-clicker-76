import time
import random
import functools

def network_retry(retries=3, base_delay=1.0, max_delay=10.0, backoff_factor=2.0):
    """
    Decorator that retries network operations with an autoclicker-inspired
    jittery exponential backoff to mimic human retry patterns.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = base_delay
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries:
                        raise e
                    human_jitter = random.uniform(-0.15, 0.15) * delay
                    sleep_time = min(max_delay, max(0.1, delay + human_jitter))
                    time.sleep(sleep_time)
                    delay *= backoff_factor
        return wrapper
    return decorator