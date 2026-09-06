import time
import ctypes
import threading

class OptimizedClicker:
    def __init__(self, interval=0.005):
        self.interval = interval
        self.running = False
        self._worker = None
        try:
            self._win32_click = ctypes.windll.user32.mouse_event
        except (AttributeError, OSError):
            self._win32_click = None

    def _loop(self):
        click_func = self._win32_click
        interval = self.interval
        if click_func:
            while self.running:
                click_func(0x0002, 0, 0, 0, 0)
                click_func(0x0004, 0, 0, 0, 0)
                time.sleep(interval)
        else:
            while self.running:
                time.sleep(interval)

    def toggle(self, state: bool):
        if state and not self.running:
            self.running = True
            self._worker = threading.Thread(target=self._loop, daemon=True)
            self._worker.start()
        elif not state:
            self.running = False