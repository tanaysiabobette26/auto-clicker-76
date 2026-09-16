import time
import threading
from queue import PriorityQueue

class BurstExecutor:
    """High-throughput event batching for click sequences."""
    def __init__(self, interval=0.001):
        self.queue = PriorityQueue()
        self.interval = interval
        self._stop = threading.Event()
        self.worker = threading.Thread(target=self._drain, daemon=True)
        self.worker.start()

    def schedule(self, action_func, priority=0):
        self.queue.put((priority, action_func))

    def _drain(self):
        while not self._stop.is_set():
            if not self.queue.empty():
                priority, task = self.queue.get()
                try:
                    task()
                finally:
                    self.queue.task_done()
            time.sleep(self.interval)

    def shutdown(self):
        self._stop.set()
        self.worker.join()

def preemptive_sleep(target_hz):
    """jitter-compensated pause for high-frequency loops."""
    deadline = time.perf_counter() + (1.0 / target_hz)
    while time.perf_counter() < deadline:
        if deadline - time.perf_counter() > 0.002:
            time.sleep(0.001)
        else:
            pass

def cache_key(func):
    """memoization decorator for static coordinate math."""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper