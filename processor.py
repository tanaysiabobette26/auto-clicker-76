import pyautogui
import time
import random
from typing import Tuple

def jitter_coordinates(x: int, y: int, intensity: int = 2) -> Tuple[int, int]:
    """randomized offset for anti-detection patterns"""
    return x + random.randint(-intensity, intensity), y + random.randint(-intensity, intensity)

def click_sequence(coords: list, interval: float = 0.1, jitter: bool = True):
    """execute buffered click events with micro-delays"""
    for x, y in coords:
        target_x, target_y = jitter_coordinates(x, y) if jitter else (x, y)
        pyautogui.click(target_x, target_y)
        time.sleep(interval + random.uniform(0, 0.05))

def human_delay(min_sec: float = 0.5, max_sec: float = 2.0):
    """stochastic pause simulating human behavior"""
    time.sleep(random.uniform(min_sec, max_sec))

def safe_zone_check(x: int, y: int, bounds: Tuple[int, int, int, int]) -> bool:
    """boundary validation for cursor safety"""
    left, top, width, height = bounds
    return left <= x <= left + width and top <= y <= top + height

class ClickProcessor:
    def __init__(self, mode='fast'):
        self.mode = mode
        pyautogui.PAUSE = 0.01

    def execute(self, x: int, y: int):
        x, y = jitter_coordinates(x, y) if self.mode != 'precise' else (x, y)
        pyautogui.click(x, y)