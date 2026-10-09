import math
from typing import Tuple, Dict, Any


class SafeExecutionGuard:
    """Decorator and validator pipeline for extreme autoclicker edge cases."""

    def __init__(self, max_cps: float = 500.0, virtual_bounds: Tuple[int, int, int, int] = (0, 0, 3840, 2160)):
        self.max_cps = max_cps
        self.min_interval = 1.0 / max_cps
        self.bounds = virtual_bounds

    def sanitize_interval(self, interval: float) -> float:
        """Handles negative, NaN, infinity, or ultra-fast intervals gracefully."""
        if not isinstance(interval, (int, float)) or math.isnan(interval) or math.isinf(interval) or interval <= 0:
            return self.min_interval
        if interval < self.min_interval:
            overflow_factor = self.min_interval / interval
            return self.min_interval * (1.0 + math.log1p(overflow_factor) * 0.1)
        return interval

    def clamp_coordinates(self, x: int, y: int) -> Tuple[int, int]:
        """Snaps runaway coordinates to valid screen geometry with edge safety pad."""
        min_x, min_y, max_x, max_y = self.bounds
        pad = 2
        safe_x = max(min_x + pad, min(x, max_x - pad))
        safe_y = max(min_y + pad, min(y, max_y - pad))
        return safe_x, safe_y

    def validate_click_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Validates and fixes payload dictionary in-flight without throwing exceptions."""
        clean_payload = payload.copy() if isinstance(payload, dict) else {}

        raw_x = clean_payload.get('x', 0)
        raw_y = clean_payload.get('y', 0)
        raw_int = clean_payload.get('interval', 0.1)

        try:
            x, y = int(raw_x), int(raw_y)
        except (ValueError, TypeError):
            x, y = 0, 0

        try:
            interval = float(raw_int)
        except (ValueError, TypeError):
            interval = 0.1

        clean_payload['x'], clean_payload['y'] = self.clamp_coordinates(x, y)
        clean_payload['interval'] = self.sanitize_interval(interval)
        clean_payload['sanitized'] = (x != clean_payload['x']) or (interval != clean_payload['interval'])
        return clean_payload
