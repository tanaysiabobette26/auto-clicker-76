import ctypes
import sys
import time
from typing import Callable


class HighPrecisionClicker:
    """Core click dispatcher optimized with dynamic microsecond spinlocks."""

    def __init__(self, target_cps: float = 100.0) -> None:
        self.interval_ns: int = int(1_000_000_000 / max(0.1, target_cps))
        self._is_running: bool = False
        self._spin_threshold_ns: int = 2_000_000
        self._platform_setup()

    def _platform_setup(self) -> None:
        if sys.platform == "win32":
            try:
                ctypes.windll.winmm.timeBeginPeriod(1)
            except Exception:
                pass

    def calibrate_spin_threshold(self) -> None:
        """Measure system scheduler drift to adaptively set spin-lock cutoff."""
        samples = []
        for _ in range(5):
            start = time.perf_counter_ns()
            time.sleep(0.001)
            delta = time.perf_counter_ns() - start
            samples.append(delta - 1_000_000)

        avg_drift = sum(max(0, s) for s in samples) // len(samples)
        self._spin_threshold_ns = max(500_000, avg_drift * 2)

    def trigger(self, click_func: Callable[[], None]) -> None:
        click_func()

    def run_burst(self, click_func: Callable[[], None], count: int) -> int:
        self.calibrate_spin_threshold()
        self._is_running = True
        executed = 0
        next_tick = time.perf_counter_ns()

        while self._is_running and executed < count:
            now = time.perf_counter_ns()
            remaining = next_tick - now

            if remaining <= 0:
                self.trigger(click_func)
                executed += 1
                next_tick += self.interval_ns
            elif remaining > self._spin_threshold_ns:
                sleep_sec = (remaining - self._spin_threshold_ns) / 1e9
                time.sleep(sleep_sec)
            else:
                while time.perf_counter_ns() < next_tick:
                    pass

        return executed

    def stop(self) -> None:
        self._is_running = False
        if sys.platform == "win32":
            try:
                ctypes.windll.winmm.timeEndPeriod(1)
            except Exception:
                pass
