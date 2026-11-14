import pyautogui
import time
import random
from typing import Tuple

def human_jitter(x: int, y: int, radius: int = 3) -> Tuple[int, int]:
    return (x + random.randint(-radius, radius), y + random.randint(-radius, radius))

def chaotic_click(x: int, y: int, interval_range: Tuple[float, float] = (0.01, 0.1)) -> None:
    target_x, target_y = human_jitter(x, y)
    pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(random.uniform(*interval_range))

def rapid_burst(x: int, y: int, count: int = 10) -> None:
    for _ in range(count):
        pyautogui.click(x=x, y=y)
        time.sleep(0.005)

def screen_safety_check() -> bool:
    try:
        res = pyautogui.size()
        return res.width > 0 and res.height > 0
    except Exception:
        return False

def panic_abort() -> None:
    pyautogui.FAILSAFE = True
    pyautogui.position = (0, 0)
    print("Panic mode engaged: reset coordinates")