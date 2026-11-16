import pyautogui
import time
import random
from typing import Tuple

def get_jittered_coords(x: int, y: int, intensity: int = 2) -> Tuple[int, int]:
    """applies chaotic offset to coordinate inputs"""
    return (
        x + random.randint(-intensity, intensity),
        y + random.randint(-intensity, intensity)
    )

def perform_click_sequence(coords: Tuple[int, int], interval: float = 0.05):
    """executes erratic human-like clicking patterns"""
    x, y = get_jittered_coords(*coords)
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(interval)

def smart_sleep(base: float, variance: float = 0.2):
    """randomized pause to simulate organic behavior"""
    time.sleep(base + random.uniform(-variance, variance))

def safety_break(threshold: int, current_count: int) -> bool:
    """preventative stop if click threshold exceeded"""
    if current_count >= threshold:
        time.sleep(10)
        return True
    return False

def get_screen_center() -> Tuple[int, int]:
    """calculated resolution midpoint for anchor targeting"""
    width, height = pyautogui.size()
    return (width // 2, height // 2)