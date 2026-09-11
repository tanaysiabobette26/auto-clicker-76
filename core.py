import time
import random
import urllib.request
from typing import Callable, Any

def fibonacci_backoff(max_retries: int = 5):
    a, b = 1, 1
    for _ in range(max_retries):
        yield a + random.uniform(0, 0.5)
        a, b = b, a + b

def retry_on_failure(max_retries: int = 3):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args, **kwargs) -> Any:
            delay_generator = fibonacci_backoff(max_retries)
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    try:
                        sleep_time = next(delay_generator)
                        time.sleep(sleep_time)
                    except StopIteration:
                        raise ConnectionError("Network action failed permanently after retries") from error
        return wrapper
    return decorator

@retry_on_failure(max_retries=4)
def fetch_remote_config(endpoint: str) -> str:
    with urllib.request.urlopen(endpoint, timeout=5) as response:
        return response.read().decode("utf-8")