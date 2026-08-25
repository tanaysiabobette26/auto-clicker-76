import ctypes
import time
import random
import threading
import math
user32 = ctypes.windll.user32
def click_mouse(button='left'):
    if button == 'left':
        user32.mouse_event(0x0002, 0, 0, 0, 0)
        user32.mouse_event(0x0004, 0, 0, 0, 0)
    elif button == 'right':
        user32.mouse_event(0x0008, 0, 0, 0, 0)
        user32.mouse_event(0x0010, 0, 0, 0, 0)
def get_mouse_pos():
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y
def set_cursor_pos(x, y):
    user32.SetCursorPos(int(x), int(y))
class ClickHelper:
    def __init__(self, clicks_per_sec=10, randomize=True):
        self.clicks_per_sec = clicks_per_sec
        self.randomize = randomize
        self._running = False
        self._thread = None
    def _loop(self):
        interval = 1.0 / self.clicks_per_sec
        while self._running:
            click_mouse()
            if self.randomize:
                sleep_t = interval * random.uniform(0.9, 1.1)
            else:
                sleep_t = interval
            time.sleep(sleep_t)
    def start(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._loop, daemon=True)
            self._thread.start()
    def stop(self):
        self._running = False
        if self._thread is not None:
            self._thread.join(2)
    def is_running(self):
        return self._running
def burst_click(count, delay=0.01):
    for _ in range(count):
        click_mouse()
        time.sleep(delay)
def variable_interval_clicks(total_clicks, min_int=0.05, max_int=0.2):
    for _ in range(total_clicks):
        click_mouse()
        interval = random.uniform(min_int, max_int)
        time.sleep(interval)
def sine_wave_intervals(clicks, base=0.1, amp=0.05):
    intervals = []
    for i in range(clicks):
        intv = base + amp * math.sin(i * 0.5)
        intervals.append(intv)
    return intervals
def apply_pattern(pattern):
    for intv in pattern:
        click_mouse()
        time.sleep(intv)