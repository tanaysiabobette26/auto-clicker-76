import time
import threading
from typing import Callable, Any, Optional

def execute_delayed(task: Callable[..., Any], delay: float, *args: Any, **kwargs: Any) -> threading.Thread:
    """Spawns a background thread to execute a function after a pause."""
    def wrapper() -> None:
        time.sleep(delay)
        task(*args, **kwargs)
    
    worker: threading.Thread = threading.Thread(target=wrapper, daemon=True)
    worker.start()
    return worker

def throttle(rate_limit: float) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator to force a cool-down period between function calls."""
    last_called: float = 0.0
    
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def inner(*args: Any, **kwargs: Any) -> Optional[Any]:
            nonlocal last_called
            elapsed: float = time.perf_counter() - last_called
            if elapsed >= rate_limit:
                last_called = time.perf_counter()
                return func(*args, **kwargs)
            return None
        return inner
    return decorator

def format_interval(seconds: float) -> str:
    """Converts seconds into a human-readable duration string."""
    ms: int = int((seconds % 1) * 1000)
    sec: int = int(seconds)
    return f"{sec}s {ms}ms"