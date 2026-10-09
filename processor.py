import math
import time
from typing import Callable, List, Tuple, Dict, Any

class ClickBoundaryError(Exception):
    """Raised when target click coordinates fall outside safe display regions."""
    pass

class RateLimitExceededError(Exception):
    """Raised when requested clicks per second exceed engine physical bounds."""
    pass

class ClickStreamProcessor:
    def __init__(self, bounds: Tuple[int, int, int, int] = (0, 0, 1920, 1080), max_cps: int = 500):
        self.bounds = bounds
        self.max_cps = max_cps
        self.circuit_broken = False
        self.error_log: List[Dict[str, Any]] = []

    def sanitize_coordinate(self, x: float, y: float) -> Tuple[int, int]:
        """Sanitizes click targets against non-numeric, infinity, or boundary overflows."""
        try:
            if math.isnan(x) or math.isnan(y) or math.isinf(x) or math.isinf(y):
                raise ClickBoundaryError(f"Invalid floating point coordinate encountered: ({x}, {y})")
            
            ix, iy = int(round(x)), int(round(y))
            min_x, min_y, max_x, max_y = self.bounds
            
            if not (min_x <= ix <= max_x and min_y <= iy <= max_y):
                clamped_x = max(min_x, min(ix, max_x))
                clamped_y = max(min_y, min(iy, max_y))
                self.error_log.append({"event": "clamped", "original": (ix, iy), "clamped": (clamped_x, clamped_y)})
                return clamped_x, clamped_y
            return ix, iy
        except (ValueError, TypeError) as err:
            raise ClickBoundaryError(f"Malformed coordinate values: {err}")

    def process_batch(self, points: List[Tuple[float, float]], cps: float, click_func: Callable[[int, int], None]) -> int:
        """Processes a batch of click targets with adaptive error handling for rate spikes."""
        if self.circuit_broken:
            return 0
        
        if cps <= 0 or cps > self.max_cps:
            self.error_log.append({"event": "rate_exhaustion", "cps": cps})
            cps = max(1.0, min(cps, float(self.max_cps)))

        interval = 1.0 / cps
        successful_clicks = 0

        for raw_x, raw_y in points:
            try:
                cx, cy = self.sanitize_coordinate(raw_x, raw_y)
                click_func(cx, cy)
                successful_clicks += 1
                time.sleep(interval)
            except ClickBoundaryError as cbe:
                self.error_log.append({"event": "skipped", "reason": str(cbe)})
                continue
            except Exception as fatal_err:
                self.circuit_broken = True
                self.error_log.append({"event": "circuit_break", "reason": str(fatal_err)})
                break

        return successful_clicks