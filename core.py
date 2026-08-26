import time
import threading
from typing import Callable

class TurboPulseCore:
    def __init__(self, cps: float = 100.0, click_callback: Callable[[], None] = lambda: None):
        self.cps = max(1.0, cps)
        self.interval = 1.0 / self.cps
        self.callback = click_callback
        self._active = threading.Event()
        self._thread = threading.Thread(target=self._pulse_loop, daemon=True)
        self._thread.start()

    def _pulse_loop(self) -> None:
        target_time = time.perf_counter()
        while True:
            self._active.wait()
            target_time += self.interval
            current_time = time.perf_counter()
            sleep_duration = target_time - current_time
            
            if sleep_duration > 0:
                time.sleep(sleep_duration)
            else:
                target_time = current_time
            
            if self._active.is_set():
                self.callback()

    def ignite(self) -> None:
        self._active.set()

    def halt(self) -> None:
        self._active.clear()

    def adjust_frequency(self, new_cps: float) -> None:
        self.cps = max(1.0, new_cps)
        self.interval = 1.0 / self.cps
