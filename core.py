import time
import threading
from typing import Callable, Optional
from dataclasses import dataclass, field


@dataclass
class ClickTask:
    target_cps: float
    click_func: Callable[[], None]
    active: bool = False
    _thread: Optional[threading.Thread] = field(default=None, repr=False)


class AutoClickerCore:
    """Reorganized click dispatch engine with automatic context-based cleanup."""

    def __init__(self) -> None:
        self._tasks: dict[str, ClickTask] = {}
        self._lock = threading.Lock()

    def register(self, name: str, cps: float, callback: Callable[[], None]) -> None:
        with self._lock:
            self._tasks[name] = ClickTask(target_cps=max(0.1, cps), click_func=callback)

    def _worker(self, task: ClickTask) -> None:
        interval = 1.0 / task.target_cps
        while task.active:
            start = time.perf_counter()
            try:
                task.click_func()
            except Exception:
                task.active = False
                break
            elapsed = time.perf_counter() - start
            time.sleep(max(0.0, interval - elapsed))

    def start(self, name: str) -> bool:
        with self._lock:
            task = self._tasks.get(name)
            if not task or task.active:
                return False
            task.active = True
            task._thread = threading.Thread(target=self._worker, args=(task,), daemon=True)
            task._thread.start()
            return True

    def stop(self, name: str) -> None:
        with self._lock:
            task = self._tasks.get(name)
            if task and task.active:
                task.active = False
                if task._thread and task._thread.is_alive():
                    task._thread.join(timeout=0.2)

    def purge_inactive(self) -> int:
        with self._lock:
            dead = [k for k, v in self._tasks.items() if not v.active]
            for k in dead:
                del self._tasks[k]
            return len(dead)

    def __enter__(self) -> "AutoClickerCore":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        with self._lock:
            for task in self._tasks.values():
                task.active = False
            self._tasks.clear()
