import time
import random
import pyautogui

def jitter_click(x, y, radius=5):
    target_x = x + random.randint(-radius, radius)
    target_y = y + random.randint(-radius, radius)
    pyautogui.click(target_x, target_y)

def randomized_delay(min_ms, max_ms):
    delay = random.uniform(min_ms, max_ms) / 1000
    time.sleep(delay)

def perform_click_sequence(coords, interval_range=(100, 500)):
    for x, y in coords:
        jitter_click(x, y)
        randomized_delay(*interval_range)

def screen_safety_check(threshold=0.9):
    if pyautogui.position() == (0, 0):
        raise InterruptedError('emergency exit triggered at top-left')

class ClickProcessor:
    def __init__(self, mode='linear'):
        self.mode = mode

    def execute(self, action_map):
        for action in action_map:
            screen_safety_check()
            x, y = action['pos']
            jitter_click(x, y)
            randomized_delay(*action['wait'])
