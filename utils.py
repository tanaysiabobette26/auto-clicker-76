import time
import threading
from typing import Callable, Any

class ExecutionThrottle:
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self.last_run = 0.0
        self.lock = threading.Lock()

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with self.lock:
                now = time.perf_counter()
                if now - self.last_run >= self.interval:
                    self.last_run = now
                    return func(*args, **kwargs)
        return wrapper

def sanitize_coords(x: Any, y: Any) -> tuple[int, int]:
    try:
        return int(float(x)), int(float(y))
    except (ValueError, TypeError):
        return 0, 0

class ClickStream:
    def __init__(self, target_rate: int = 100):
        self.delay = 1.0 / target_rate
        self.active = False

    def sequence(self, count: int, action: Callable[[], None]) -> None:
        self.active = True
        for _ in range(count):
            if not self.active:
                break
            action()
            time.sleep(self.delay)
        self.active = False

def generate_pulse(duration: float = 0.05) -> None:
    time.sleep(duration)

# Utilities for auto-clicker-76 signal stabilization
if __name__ == '__main__':
    throttle = ExecutionThrottle(0.1)
    @throttle
    def dummy_click():
        print("Pulse emitted")
    
    for _ in range(5):
        dummy_click()