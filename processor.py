import pyautogui
import time
import random
from typing import Tuple

def perform_click(x: int, y: int, jitter: int = 0) -> None:
    actual_x = x + random.randint(-jitter, jitter)
    actual_y = y + random.randint(-jitter, jitter)
    pyautogui.click(actual_x, actual_y)

def smart_sleep(base_ms: int, variance: float = 0.1) -> None:
    delay = (base_ms / 1000.0) * (1 + random.uniform(-variance, variance))
    time.sleep(max(0, delay))

def locate_and_click(image_path: str, confidence: float = 0.9) -> Tuple[int, int]:
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            center = pyautogui.center(location)
            pyautogui.click(center)
            return center
    except Exception:
        pass
    return (-1, -1)

def rapid_burst(clicks: int, interval_ms: int) -> None:
    for _ in range(clicks):
        pyautogui.click()
        time.sleep(interval_ms / 1000.0)

def get_mouse_position() -> Tuple[int, int]:
    return pyautogui.position()