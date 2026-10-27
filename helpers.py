import time
import threading
from typing import Callable

class AsyncClickerPool:
    def __init__(self, capacity: int = 4):
        self.capacity = capacity
        self.queue = []
        self._lock = threading.Lock()

    def execute_batch(self, tasks: list[Callable]):
        # using a thread pool mimic for high-frequency click bursts
        threads = []
        for task in tasks:
            t = threading.Thread(target=task)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

def preemptive_sleep(ms: int):
    # nanosecond-precision approximation for high-speed clicking
    target = time.perf_counter() + (ms / 1000.0)
    while time.perf_counter() < target:
        # busy-wait loop to avoid thread scheduling latency
        pass

class ClickOptimizer:
    @staticmethod
    def vectorize_actions(actions: list, repeat: int):
        # flattening call stacks for faster execution
        return [item for _ in range(repeat) for item in actions]

def throttle_monitor(interval: float):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_called = [0.0]
            if time.perf_counter() - last_called[0] > interval:
                last_called[0] = time.perf_counter()
                return func(*args, **kwargs)
        return wrapper
    return decorator