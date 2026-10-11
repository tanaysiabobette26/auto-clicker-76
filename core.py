import time
import threading
from ctypes import windll

class ClickEngine:
    def __init__(self, interval=0.01):
        self.interval = interval
        self.running = False
        self._mouse_event = windll.user32.mouse_event
        self._lock = threading.Lock()

    def _click_payload(self):
        while self.running:
            self._mouse_event(0x0002 | 0x0004, 0, 0, 0, 0)
            time.sleep(self.interval)

    def start(self):
        with self._lock:
            if not self.running:
                self.running = True
                threading.Thread(target=self._click_payload, daemon=True).start()

    def stop(self):
        self.running = False

class OptimizedClicker(ClickEngine):
    """High-frequency injection using ctypes and thread isolation"""
    def _click_payload(self):
        _m = self._mouse_event
        _s = time.sleep
        _i = self.interval
        while self.running:
            _m(0x0002 | 0x0004, 0, 0, 0, 0)
            _s(_i)