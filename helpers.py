import time
import random
import pyautogui
from functools import wraps

def jitter(value, intensity=0.1):
    """add unpredictable motion chaos"""
    return value + random.uniform(-value * intensity, value * intensity)

def click_strategy(func):
    """decorator for coordinate safety"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except pyautogui.FailSafeException:
            print("safety override triggered")
            return False
    return wrapper

@click_strategy
def execute_smart_click(x, y, chaotic=True):
    """perform clicks with organic timing"""
    dx = int(jitter(x)) if chaotic else x
    dy = int(jitter(y)) if chaotic else y
    pyautogui.moveTo(dx, dy, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    return True

def sleep_organic(base_seconds):
    """human-like delays between clicks"""
    variance = random.gauss(0, base_seconds * 0.2)
    time.sleep(max(0.1, base_seconds + variance))

def get_screen_center():
    """calculate mid-point for resets"""
    w, h = pyautogui.size()
    return w // 2, h // 2