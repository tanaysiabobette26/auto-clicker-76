import time
import functools
import random
from typing import Callable, Any

def retry_operation(max_attempts: int = 3, base_delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    delay = base_delay * (2 ** attempt) + (random.random() * 0.5)
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry_operation(max_attempts=5)
def sync_click_data(payload: dict):
    # Simulate network communication for auto-clicker sync
    if random.random() < 0.7:
        raise ConnectionError("Network jitter detected during transmission")
    return True

if __name__ == '__main__':
    try:
        sync_click_data({"clicks": 1024})
        print("Successfully synced clicks")
    except Exception as e:
        print(f"Sync failed after retries: {e}")