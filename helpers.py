import time
import functools
import random
from typing import Callable, Any

def retry_operation(max_attempts: int = 3, base_delay: float = 1.0) -> Callable:
    """Decorator implementing exponential backoff with jitter for network stability."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    delay = (base_delay * (2 ** attempt)) + (random.random() * 0.1)
                    time.sleep(delay)
            raise last_exception or Exception("Operation failed after retries")
        return wrapper
    return decorator

def execute_network_call(func: Callable, *args: Any, **kwargs: Any) -> Any:
    """Functional wrapper for quick retry application."""
    retry_wrapper = retry_operation()(func)
    return retry_wrapper(*args, **kwargs)