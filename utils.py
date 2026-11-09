import time
import collections
from functools import lru_cache

class ClickOptimizer:
    def __init__(self, interval_ms=10):
        self.interval = interval_ms / 1000.0
        self.history = collections.deque(maxlen=100)

    @lru_cache(maxsize=128)
    def calculate_jitter(self, base_ms: int) -> float:
        import random
        return base_ms * (1 + (random.random() * 0.05))

    def get_optimized_delay(self, current_latency: float) -> float:
        self.history.append(current_latency)
        avg_latency = sum(self.history) / len(self.history)
        return max(0.001, self.interval - avg_latency)

def busy_wait(duration: float):
    start = time.perf_counter()
    while time.perf_counter() - start < duration:
        pass

def execute_optimized_click(optimizer: ClickOptimizer, latency: float):
    delay = optimizer.get_optimized_delay(latency)
    if delay > 0.005:
        time.sleep(delay - 0.002)
    busy_wait(0.002)

def get_precise_timestamp() -> int:
    return int(time.perf_counter() * 1000000)