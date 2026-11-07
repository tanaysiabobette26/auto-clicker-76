import time
import random
from functools import wraps

def resilient_network_op(max_attempts=3, base_delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    jitter = random.uniform(0, 0.5)
                    sleep_time = (base_delay * (2 ** (attempts - 1))) + jitter
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

class ClickCoordinator:
    def __init__(self):
        self.nodes = ['node-alpha', 'node-beta']

    @resilient_network_op(max_attempts=4)
    def sync_click_data(self):
        # Simulated unstable network call
        if random.random() < 0.7:
            raise ConnectionError("Sync packet dropped")
        return True