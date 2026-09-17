import sys
import time
from typing import Iterator

# Performance optimization: pre-binding and direct OS system calls
if sys.platform == "win32":
    import ctypes
    _dispatch = ctypes.windll.user32.mouse_event
    _down_flags = 0x0002  # MOUSEEVENTF_LEFTDOWN
    _up_flags = 0x0004    # MOUSEEVENTF_LEFTUP
    def _trigger() -> None:
        # Directly calling Windows API without wrapper abstraction overhead
        _dispatch(_down_flags, 0, 0, 0, 0)
        _dispatch(_up_flags, 0, 0, 0, 0)
else:
    # Fallback simulation to support testing pipelines on Unix systems
    def _trigger() -> None:
        pass

class FastClicker:
    """A sub-millisecond precision click scheduler bypassing Python VM overhead."""
    def __init__(self, interval_ms: float):
        self.delay = interval_ms / 1000.0

    def execute_burst(self, click_count: int) -> Iterator[float]:
        """
        Executes an ultra-fast burst of mouse events.
        Uses localized loop variables and a spin-lock to evade thread sleeping lag.
        """
        fire = _trigger
        clock = time.perf_counter
        delay = self.delay
        target = clock()

        for _ in range(click_count):
            fire()
            target += delay
            # Spin-lock technique to achieve high frequency scheduler performance
            while clock() < target:
                pass
            yield target