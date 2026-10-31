import time
import logging
from typing import Callable, Any, Optional

logger = logging.getLogger('auto-clicker-76')

class ClickerError(Exception):
    """Base exception for auto-clicker-76 events."""
    pass

def safety_wrapper(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes click events with extreme prejudice against runtime chaos."""
    try:
        return func(*args, **kwargs)
    except PermissionError:
        logger.error("Insufficient OS privileges for click injection")
        return None
    except ValueError as e:
        logger.warning(f"Invalid coordinate geometry: {e}")
        return None
    except Exception as e:
        logger.critical(f"Catastrophic click failure: {type(e).__name__}")
        return False

def validate_interval(interval: float) -> float:
    """Enforces sanity bounds on click frequency."""
    if not isinstance(interval, (int, float)):
        raise ClickerError("Interval must be numeric")
    if interval < 0.01:
        logger.warning("High-frequency interval detected, potentially unstable")
        return 0.01
    return float(interval)

def retry_operation(func: Callable, retries: int = 3) -> Any:
    """Resilience pattern for transient input device hiccups."""
    for attempt in range(retries):
        try:
            return func()
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(0.1 * (2 ** attempt))
    return None