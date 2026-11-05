import time
import functools

class ClickValidator:
    def __init__(self, limit=1000):
        self.limit = limit
        self.history = [0.0] * limit
        self.idx = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            self.history[self.idx] = now
            self.idx = (self.idx + 1) % self.limit
            
            if self.idx == 0:
                delta = now - self.history[self.idx]
                if delta < 1.0:
                    return None
            return func(*args, **kwargs)
        return wrapper

class RateLimitExceeded(Exception):
    pass

def validate_frequency(min_interval=0.001):
    last_call = [0.0]
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.perf_counter()
            if current_time - last_call[0] < min_interval:
                return None
            last_call[0] = current_time
            return func(*args, **kwargs)
        return wrapper
    return decorator