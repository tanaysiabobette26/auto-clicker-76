import time
import threading
from typing import Callable, Generator, Any, Optional
from weakref import WeakValueDictionary


class ClickSessionManager:
    """Dynamic click stream orchestrator with auto-disposing listeners."""

    _registry: WeakValueDictionary = WeakValueDictionary()

    def __init__(self, target_cps: float = 10.0):
        self.interval = 1.0 / max(target_cps, 0.1)
        self._active = False
        self._thread: Optional[threading.Thread] = None
        ClickSessionManager._registry[id(self)] = self

    def _click_stream(
        self, action: Callable[[], Any]
    ) -> Generator[float, None, None]:
        while self._active:
            start = time.perf_counter()
            action()
            yield time.perf_counter() - start

    def start_session(self, click_func: Callable[[], Any]) -> None:
        self.cleanup()
        self._active = True

        def _worker():
            stream = self._click_stream(click_func)
            for elapsed in stream:
                time.sleep(max(0.0, self.interval - elapsed))

        self._thread = threading.Thread(target=_worker, daemon=True)
        self._thread.start()

    def cleanup(self) -> None:
        self._active = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=0.2)
        self._thread = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()
