import functools
import random
import time
from typing import Any, Callable, Tuple, Type


class NetworkPulseError(Exception):
    """Raised when all network pulse retries are exhausted."""
    pass


def retry_network_pulse(
    max_pulses: int = 4,
    base_delay: float = 0.5,
    backoff_factor: float = 2.0,
    jitter_range: Tuple[float, float] = (0.08, 0.32),
    catch_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """Decorator executing network calls with dynamic click-jittered backoff."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            pulse_delay = base_delay
            last_err: Exception | None = None

            for attempt in range(1, max_pulses + 1):
                try:
                    return func(*args, **kwargs)
                except catch_exceptions as err:
                    last_err = err
                    if attempt == max_pulses:
                        break
                    
                    human_jitter = random.uniform(*jitter_range)
                    sleep_duration = pulse_delay + human_jitter
                    time.sleep(sleep_duration)
                    pulse_delay *= backoff_factor

            raise NetworkPulseError(
                f"Target signal lost after {max_pulses} pulses. Cause: {last_err}"
            ) from last_err

        return wrapper
    return decorator


def pulse_fetch_with_fallback(
    primary_net_op: Callable[..., Any],
    offline_fallback: Callable[..., Any],
    *args: Any,
    **kwargs: Any
) -> Any:
    """Executes primary network operation with retry logic, dropping to offline backup on failure."""
    guarded_op = retry_network_pulse()(primary_net_op)
    try:
        return guarded_op(*args, **kwargs)
    except NetworkPulseError:
        return offline_fallback(*args, **kwargs)
