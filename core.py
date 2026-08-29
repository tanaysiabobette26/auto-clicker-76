import time
from collections import deque
import threading

class AutoClickerCore:
    """Optimized core for auto clicker with creative timing adjustment."""
    def __init__(self, clicks_per_second=10.0, duration=None):
        self.cps = clicks_per_second
        self.interval = 1.0 / clicks_per_second
        self.duration = duration
        self.running = False
        self.click_count = 0
        self.drift_history = deque(maxlen=5)
        self._lock = threading.Lock()
        self._thread = None

    def _calculate_optimized_interval(self):
        if not self.drift_history:
            return self.interval
        weights = [0.1, 0.2, 0.3, 0.4, 0.5][:len(self.drift_history)]
        total_weight = sum(weights)
        avg_drift = sum(d * w for d, w in zip(self.drift_history, weights)) / total_weight
        optimized = self.interval - avg_drift * 0.5
        return max(0.001, min(optimized, self.interval * 2))

    def _perform_click(self):
        with self._lock:
            self.click_count += 1
            precise_time = time.perf_counter()
            print(f"Optimized click #{self.click_count} at {precise_time:.9f}")

    def _run_optimized_loop(self):
        start = time.perf_counter()
        next_click = start
        end_time = start + self.duration if self.duration else float('inf')

        while self.running and time.perf_counter() < end_time:
            current = time.perf_counter()
            if current >= next_click:
                self._perform_click()
                actual = time.perf_counter()
                drift = actual - next_click
                self.drift_history.append(drift)
                next_click += self._calculate_optimized_interval()
                if next_click - actual < 0.002:
                    continue
            else:
                sleep_duration = next_click - current
                time.sleep(sleep_duration * 0.95)

        self.running = False

    def start(self):
        if self.running:
            return
        self.running = True
        self.click_count = 0
        self.drift_history.clear()
        self._thread = threading.Thread(target=self._run_optimized_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self.running = False
        if self._thread:
            self._thread.join(timeout=1.0)

    def get_stats(self):
        return {
            'clicks': self.click_count,
            'current_interval': self._calculate_optimized_interval()
        }
