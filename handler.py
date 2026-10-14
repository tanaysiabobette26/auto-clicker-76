import pyautogui
import time
import random
from typing import Tuple

def jitter_click(x: int, y: int, intensity: int = 5) -> None:
    """Simulates human-like movement with slight noise."""
    dx = x + random.randint(-intensity, intensity)
    dy = y + random.randint(-intensity, intensity)
    pyautogui.click(dx, dy)

def smart_burst(x: int, y: int, count: int, interval: float) -> None:
    """Rapid fire sequence with micro-delays to avoid detection."""
    for _ in range(count):
        pyautogui.click(x, y)
        time.sleep(interval + random.uniform(0.01, 0.05))

def safety_pause(duration_range: Tuple[float, float]) -> None:
    """Randomized sleep to break rigid patterns."""
    time.sleep(random.uniform(*duration_range))

def drag_and_drop_sequence(start: Tuple[int, int], end: Tuple[int, int]) -> None:
    """Controlled coordinate transition for drag actions."""
    pyautogui.moveTo(*start)
    pyautogui.mouseDown()
    pyautogui.moveTo(*end, duration=random.uniform(0.2, 0.5))
    pyautogui.mouseUp()

def emergency_abort_check(key: str = 'q') -> bool:
    """Input trap for graceful termination."""
    import keyboard
    return keyboard.is_pressed(key)