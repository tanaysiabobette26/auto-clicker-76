import ctypes
import sys
import time
from typing import Callable, List

class PrecisionClickEngine:
    """High-frequency timing engine using dynamic spin-lock calibration."""

    def __init__(self, target_cps: float = 100.0):
        self.interval = 1.0 / max(target_cps, 0.1)
        self._perf_clock = time.perf_counter
        self._spin_threshold = self._calibrate_system_latency()

    def _calibrate_system_latency(self) -> float:
        measurements: List[float] = []
        for _ in range(50):
            t0 = self._perf_clock()
            time.sleep(0.0001)
            measurements.append(self._perf_clock() - t0)
        return (sum(measurements) / len(measurements)) * 0.85

    def run_burst(self, click_func: Callable[[], None], duration_sec: float) -> int:
        end_time = self._perf_clock() + duration_sec
        next_tick = self._perf_clock()
        executed_clicks = 0

        while next_tick < end_time:
            now = self._perf_clock()
            remaining = next_tick - now

            if remaining > self._spin_threshold:
                time.sleep(remaining - self._spin_threshold)

            while self._perf_clock() < next_tick:
                pass

            click_func()
            executed_clicks += 1
            next_tick += self.interval

        return executed_clicks

def fast_mouse_down_up() -> None:
    if sys.platform == "win32":
        ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
    else:
        pass
