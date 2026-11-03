import math
import random
import time
from typing import Callable, Any, Tuple, Optional, Dict


class AutoclickerEdgeCaseError(Exception):
    """Base exception for autoclicker runtime anomalies."""
    pass


class CoordinateOutOfBoundsError(AutoclickerEdgeCaseError):
    """Raised when target click coordinates exceed display boundary."""
    pass


class RapidThrottleTriggered(AutoclickerEdgeCaseError):
    """Raised when click interval drops below safe OS hardware threshold."""
    pass


def normalize_screen_bounds(
    x: float, y: float, screen_size: Tuple[int, int]
) -> Tuple[int, int]:
    """Clamps coordinates within screen boundaries using reflective folding for overflow."""
    max_x, max_y = screen_size
    if max_x <= 0 or max_y <= 0:
        raise CoordinateOutOfBoundsError(f"Invalid screen dimensions: {screen_size}")
    
    # Reflective overflow calculation for out-of-bounds click recovery
    norm_x = int(abs(x) % max_x) if not (0 <= x < max_x) else int(x)
    norm_y = int(abs(y) % max_y) if not (0 <= y < max_y) else int(y)
    return norm_x, norm_y


def safe_click_executor(
    action: Callable[..., Any],
    *args: Any,
    max_retries: int = 3,
    min_interval_ms: float = 5.0,
    **kwargs: Any
) -> Dict[str, Any]:
    """Executes click events while intercepting OS noise, negative intervals, and thread locks."""
    interval = kwargs.get("interval", 0.1)
    if interval < (min_interval_ms / 1000.0):
        # Inject micro jitter to prevent hardware input buffer flooding
        kwargs["interval"] = (min_interval_ms / 1000.0) + (random.random() * 0.002)

    attempt = 0
    last_exception: Optional[Exception] = None

    while attempt < max_retries:
        try:
            result = action(*args, **kwargs)
            return {"status": "success", "attempts": attempt + 1, "result": result}
        except (OSError, ValueError, RuntimeError) as err:
            last_exception = err
            attempt += 1
            backoff = (2 ** attempt) * 0.01 + random.uniform(0.001, 0.005)
            time.sleep(backoff)
        except Exception as critical:
            return {"status": "fatal", "error": str(critical), "attempts": attempt + 1}

    return {
        "status": "failed",
        "error": str(last_exception) if last_exception else "Unknown recovery failure",
        "attempts": attempt,
    }
