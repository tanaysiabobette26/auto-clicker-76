import time
import threading
import pyautogui
from typing import Callable, Optional

class ClickHandler:
    def __init__(self):
        self._stop_event = threading.Event()

    def execute_pattern(self, coords: list[tuple[int, int]], interval: float = 0.1):
        """Executes a sequence of clicks using a coordinate list."""
        self._stop_event.clear()
        for x, y in coords:
            if self._stop_event.is_set():
                break
            pyautogui.click(x, y)
            time.sleep(interval)

    def emergency_stop(self):
        """Sets the flag to halt ongoing click routines."""
        self._stop_event.set()

    def timed_macro(self, func: Callable, duration: float, frequency: float):
        """Runs a decorator-injected function for a specific duration."""
        end_time = time.time() + duration
        while time.time() < end_time and not self._stop_event.is_set():
            func()
            time.sleep(1 / frequency)

    @staticmethod
    def jitter_click(x: int, y: int, radius: int = 5):
        """Click with randomized coordinates for anti-detection."""
        import random
        dx = random.randint(-radius, radius)
        dy = random.randint(-radius, radius)
        pyautogui.click(x + dx, y + dy)

    def threaded_wrapper(self, target: Callable):
        """Execution of tasks in background threads."""
        thread = threading.Thread(target=target, daemon=True)
        thread.start()
        return thread