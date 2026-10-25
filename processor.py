import pyautogui
import time
import threading
from typing import Callable, Optional

class ClickProcessor:
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._active = False
        self._thread: Optional[threading.Thread] = None

    def _run(self, click_func: Callable[[], None]) -> None:
        while self._active:
            click_func()
            time.sleep(self.interval)

    def start(self, click_func: Callable[[], None] = pyautogui.click) -> None:
        if not self._active:
            self._active = True
            self._thread = threading.Thread(target=self._run, args=(click_func,), daemon=True)
            self._thread.start()

    def stop(self) -> None:
        self._active = False
        if self._thread:
            self._thread.join()

class CoordinateFilter:
    def __init__(self, bounds: tuple[int, int, int, int]):
        self.x, self.y, self.w, self.h = bounds

    def is_inside(self, x: int, y: int) -> bool:
        return self.x <= x <= (self.x + self.w) and self.y <= y <= (self.y + self.h)

def create_processor(interval: float) -> ClickProcessor:
    return ClickProcessor(interval=interval)