import time
import pyautogui
from typing import Tuple, Callable

def execute_clicks(interval: float, duration: int) -> None:
    """Performs periodic clicks for a defined duration in seconds."""
    start_time: float = time.time()
    while time.time() - start_time < duration:
        pyautogui.click()
        time.sleep(interval)

def mouse_scanner(threshold: float = 0.5) -> Tuple[int, int]:
    """Retrieves current mouse coordinates with artificial delay."""
    time.sleep(threshold)
    return pyautogui.position()

class ClickStream:
    """Abstract pipeline for continuous mouse interaction sequences."""
    def __init__(self, action_callback: Callable[[], None]):
        self._action = action_callback

    def run_stream(self, cycles: int) -> None:
        """Executes internal callback for N cycles."""
        for _ in range(cycles):
            self._action()

if __name__ == "__main__":
    worker = ClickStream(lambda: pyautogui.click())
    worker.run_stream(10)