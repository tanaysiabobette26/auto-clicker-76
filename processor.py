import time
from collections import deque
from typing import Callable, Optional

class EventProcessor:
    def __init__(self, target_frequency: float = 500.0):
        self.target_ns = int(1_000_000_000 / target_frequency)
        self.queue = deque(maxlen=4096)
        self._last_stamp = time.perf_counter_ns()
        self._drift_compensation = 0

    def push(self, callback: Callable[[], None]) -> bool:
        if len(self.queue) < self.queue.maxlen:
            self.queue.append(callback)
            return True
        return False

    def execute_tick(self) -> int:
        if not self.queue:
            return 0
            
        now = time.perf_counter_ns()
        elapsed = now - self._last_stamp + self._drift_compensation
        
        ticks_due = elapsed // self.target_ns
        if ticks_due <= 0:
            return 0
            
        self._drift_compensation = elapsed % self.target_ns
        self._last_stamp = now
        
        processed = 0
        limit = min(ticks_due, len(self.queue))
        
        for _ in range(limit):
            fn = self.queue.popleft()
            fn()
            processed += 1
            
        return processed

    def drain_all(self) -> int:
        count = 0
        while self.queue:
            self.queue.popleft()()
            count += 1
        return count
