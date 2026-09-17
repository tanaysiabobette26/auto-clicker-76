import time
import random
from typing import Callable, Any, Tuple

def jitter_delay(base_ms: int, variance: int = 50) -> None:
    sleep_time = (base_ms + random.randint(-variance, variance)) / 1000
    time.sleep(max(0.001, sleep_time))

def execute_with_retry(func: Callable, retries: int = 3, *args: Any, **kwargs: Any) -> Any:
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(0.1)
    return None

def get_screen_center(width: int, height: int) -> Tuple[int, int]:
    return (width // 2, height // 2)

def sanitize_interval(val: float, min_val: float = 0.01, max_val: float = 10.0) -> float:
    return max(min_val, min(val, max_val))

class ClickContext:
    def __init__(self, target_coord: Tuple[int, int]):
        self.x, self.y = target_coord
        self.timestamp = time.perf_counter()

    def __repr__(self) -> str:
        return f"Click(x={self.x}, y={self.y}) at {self.timestamp:.4f}"