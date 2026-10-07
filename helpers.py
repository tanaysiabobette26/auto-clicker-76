import time
import threading
from typing import Callable, Optional

class ClickExecutor:
    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def _worker(self, action: Callable[[], None]) -> None:
        while self._running:
            action()
            time.sleep(self.interval)

    def start(self, action: Callable[[], None]) -> None:
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._worker, args=(action,), daemon=True)
            self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread:
            self._thread.join()

def debounce(wait: float) -> Callable:
    def decorator(func: Callable) -> Callable:
        last_called = [0.0]
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] >= wait:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def format_runtime(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}m {s:02d}s elapsed"