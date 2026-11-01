import pyautogui
import time
import random
from typing import Tuple

def jitter_coordinates(pos: Tuple[int, int], radius: int = 3) -> Tuple[int, int]:
    return (pos[0] + random.randint(-radius, radius), pos[1] + random.randint(-radius, radius))

def human_click(target: Tuple[int, int], hold_time: float = 0.05) -> None:
    actual_pos = jitter_coordinates(target)
    pyautogui.moveTo(*actual_pos, duration=random.uniform(0.1, 0.3))
    pyautogui.mouseDown()
    time.sleep(hold_time)
    pyautogui.mouseUp()

def rapid_burst(target: Tuple[int, int], count: int, interval: float) -> None:
    for _ in range(count):
        pyautogui.click(*jitter_coordinates(target))
        time.sleep(interval * random.uniform(0.8, 1.2))

def safe_zone_check(x: int, y: int, bounds: Tuple[int, int, int, int]) -> bool:
    x1, y1, x2, y2 = bounds
    return x1 <= x <= x2 and y1 <= y <= y2

def sleep_with_variance(base_seconds: float, variance: float = 0.1) -> None:
    time.sleep(base_seconds * (1 + random.uniform(-variance, variance)))

class ClickExecutor:
    def __init__(self, fallback_pos: Tuple[int, int] = (0, 0)):
        self.fallback = fallback_pos

    def execute(self, pos: Tuple[int, int] = None) -> None:
        target = pos or self.fallback
        human_click(target)