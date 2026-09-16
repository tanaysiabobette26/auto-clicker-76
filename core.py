import ctypes
import platform
import time
from typing import Callable, List, Tuple


class UltraPreciseClicker:
    """High-frequency event execution engine using dynamic hybrid-spin timing."""

    def __init__(self, click_func: Callable[[], None]):
        self.click_func = click_func
        self._is_win = platform.system() == "Windows"
        self._setup_timer()

    def _setup_timer(self) -> None:
        if self._is_win:
            try:
                ctypes.windll.winmm.timeBeginPeriod(1)
            except Exception:
                pass

    def _precise_wait(self, target_time: float) -> None:
        """Hybrid sleep/spin wait for ultra-low jitter sub-millisecond precision."""
        while True:
            now = time.perf_counter()
            diff = target_time - now
            if diff <= 0:
                break
            if diff > 0.002:
                time.sleep(diff - 0.001)

    def execute_burst(self, total_clicks: int, interval_sec: float) -> int:
        """Executes a pre-scheduled burst sequence with minimum thread overhead."""
        executed = 0
        start_time = time.perf_counter()

        # Pre-calculate schedule to eliminate runtime drift calculation
        schedule = [start_time + (i * interval_sec) for i in range(total_clicks)]

        for target in schedule:
            self._precise_wait(target)
            self.click_func()
            executed += 1

        return executed

    def teardown(self) -> None:
        if self._is_win:
            try:
                ctypes.windll.winmm.timeEndPeriod(1)
            except Exception:
                pass


def benchmark_engine(rate_hz: int = 1000, duration_sec: float = 0.1) -> float:
    clicks = 0

    def dummy_target():
        nonlocal clicks
        clicks += 1

    engine = UltraPreciseClicker(dummy_target)
    total = int(rate_hz * duration_sec)
    interval = 1.0 / rate_hz

    start = time.perf_counter()
    engine.execute_burst(total, interval)
    elapsed = time.perf_counter() - start
    engine.teardown()

    return clicks / elapsed if elapsed > 0 else 0.0
