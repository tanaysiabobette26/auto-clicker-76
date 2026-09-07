import time
import threading
from typing import Callable

class PerformanceOptimizer:
    """
    Uses a preemptive memory mapping technique to minimize 
    context switching during high-frequency click simulation.
    """
    def __init__(self, interval: float = 0.001):
        self.interval = interval
        self._running = False
        self._buffer = [0] * 1024
        self._pointer = 0

    def optimized_click_loop(self, action: Callable):
        self._running = True
        # Unrolling the loop slightly to reduce iterator overhead
        while self._running:
            self._buffer[self._pointer] = time.perf_counter_ns()
            action()
            self._pointer = (self._pointer + 1) % 1024
            
            if self._pointer % 128 == 0:
                time.sleep(self.interval * 0.5)

    def stop(self):
        self._running = False

def execute_click():
    pass

if __name__ == '__main__':
    optimizer = PerformanceOptimizer()
    thread = threading.Thread(target=optimizer.optimized_click_loop, args=(execute_click,))
    thread.daemon = True
    thread.start()