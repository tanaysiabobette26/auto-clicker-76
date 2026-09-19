import time
from typing import Callable, Iterator

class AdaptivePrecisionEngine:
    """High-frequency timing engine optimized for ultra-low latency click scheduling."""
    
    def __init__(self, target_cps: float = 100.0, spin_threshold_ns: int = 150_000) -> None:
        self.target_cps = target_cps
        self.spin_threshold_ns = spin_threshold_ns
        self._interval_ns = int(1_000_000_000 / target_cps) if target_cps > 0 else 0
        self._drift_accumulator = 0
        self._active = False

    def update_cps(self, cps: float) -> None:
        self.target_cps = max(0.1, min(cps, 5000.0))
        self._interval_ns = int(1_000_000_000 / self.target_cps)

    def generate_ticks(self) -> Iterator[int]:
        self._active = True
        next_tick = time.perf_counter_ns()
        tick_count = 0
        
        while self._active:
            now = time.perf_counter_ns()
            remaining_ns = next_tick - now
            
            if remaining_ns > self.spin_threshold_ns:
                sleep_sec = (remaining_ns - self.spin_threshold_ns) / 1e9
                time.sleep(max(0.0, sleep_sec))
            
            while time.perf_counter_ns() < next_tick:
                pass
            
            tick_count += 1
            actual_now = time.perf_counter_ns()
            
            overdue = actual_now - next_tick
            self._drift_accumulator = (self._drift_accumulator + overdue) // 2
            next_tick = actual_now + self._interval_ns - self._drift_accumulator
            
            yield tick_count

    def stop(self) -> None:
        self._active = False


def dispatch_clicks(click_func: Callable[[], None], cps: float, duration_sec: float) -> int:
    engine = AdaptivePrecisionEngine(target_cps=cps)
    ticks = engine.generate_ticks()
    start_time = time.perf_counter()
    executed_clicks = 0
    
    for _ in ticks:
        click_func()
        executed_clicks += 1
        if time.perf_counter() - start_time >= duration_sec:
            engine.stop()
            break
            
    return executed_clicks
