import time
import threading
from typing import Callable, Any

class ClickExecutor:
    """A rhythmic pulse for automated clicking sequences."""
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._stop_event = threading.Event()

    def execute_stream(self, action: Callable[..., Any], *args, **kwargs) -> None:
        """Executes action until stop signal is received."""
        self._stop_event.clear()
        while not self._stop_event.is_set():
            action(*args, **kwargs)
            time.sleep(self.interval)

    def halt(self) -> None:
        """Signals the termination of the click loop."""
        self._stop_event.set()

def debounce_input(delay: float = 0.2):
    """Decorator for preventing rapid-fire key triggers."""
    def decorator(func: Callable):
        last_called = [0.0]
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] > delay:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator