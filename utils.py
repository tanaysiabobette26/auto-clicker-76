import time
import threading
from typing import Callable, Any, Optional

def debounce(wait_seconds: float) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator for rate-limiting rapid click events."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        last_called: float = 0.0
        def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
            nonlocal last_called
            elapsed: float = time.time() - last_called
            if elapsed > wait_seconds:
                last_called = time.time()
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

def run_async(target: Callable[..., None], *args: Any) -> threading.Thread:
    """Spawns a background thread for non-blocking clicks."""
    thread: threading.Thread = threading.Thread(target=target, args=args, daemon=True)
    thread.start()
    return thread

def format_timestamp(ts: float) -> str:
    """String conversion for logging event cycles."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

class ClickSequence:
    """Iterator pattern for sequence-based click automation."""
    def __init__(self, coordinates: list[tuple[int, int]]) -> None:
        self.coords: list[tuple[int, int]] = coordinates
        self._idx: int = 0

    def __next__(self) -> tuple[int, int]:
        val: tuple[int, int] = self.coords[self._idx]
        self._idx = (self._idx + 1) % len(self.coords)
        return val