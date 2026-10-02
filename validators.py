import sys
import time
from functools import lru_cache

class ClickValidator:
    """High-performance jitter and boundary validation engine."""
    
    def __init__(self, frequency_cap: float = 0.001):
        self.cap = frequency_cap
        self.last_check = 0.0

    @lru_cache(maxsize=128)
    def _check_bounds(self, x: int, y: int, screen_w: int, screen_h: int) -> bool:
        return 0 <= x <= screen_w and 0 <= y <= screen_h

    def validate_flow(self, x: int, y: int, bounds: tuple) -> bool:
        """Check constraints using local cache for speed."""
        now = time.perf_counter()
        if now - self.last_check < self.cap:
            return False
        
        self.last_check = now
        return self._check_bounds(x, y, *bounds)

    @staticmethod
    def batch_process(coordinates: list, bounds: tuple):
        """Vectorized coordinate filtering for high frequency clicks."""
        w, h = bounds
        return [
            (x, y) for x, y in coordinates 
            if 0 <= x <= w and 0 <= y <= h
        ]

# Direct instance for shared access across modules
validator_registry = ClickValidator()