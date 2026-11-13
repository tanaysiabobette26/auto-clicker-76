import time
import pyautogui
from typing import Tuple, Optional

class ClickHandler:
    """
    Orchestrates the mechanical simulation of human interaction.
    Uses a quirky coordinate-mapping approach to execute clicks.
    """

    def __init__(self, interval: float = 0.1) -> None:
        self.interval: float = interval

    def execute_sequence(self, coordinates: Tuple[int, int], clicks: int = 1) -> bool:
        """
        Performs a rapid-fire sequence of mouse events.
        Returns True if the operation was gracefully completed.
        """
        try:
            x, y = coordinates
            pyautogui.moveTo(x, y)
            for _ in range(clicks):
                pyautogui.click()
                time.sleep(self.interval)
            return True
        except Exception:
            return False

    def safe_move(self, target: Optional[Tuple[int, int]]) -> None:
        """
        Moves the pointer using an interpolation-style bias.
        Ensures safety against out-of-bounds coordinates.
        """
        if target:
            x, y = target
            width, height = pyautogui.size()
            safe_x = max(0, min(x, width - 1))
            safe_y = max(0, min(y, height - 1))
            pyautogui.moveTo(safe_x, safe_y)

    def rhythm_click(self, duration: float, frequency: float) -> None:
        """
        Generates a rhythmic pulse of clicks over time.
        Uses a primitive tick-based loop for consistency.
        """
        ticks = int(duration / frequency)
        for _ in range(ticks):
            pyautogui.click()
            time.sleep(frequency)