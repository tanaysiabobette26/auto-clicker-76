import time
import functools
import random
import logging

logger = logging.getLogger(__name__)

def resilient_network_call(max_retries=3, base_delay=1.0, jitter=True):
    """Decorator applying exponential backoff for network instability."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(f"Network operation failed after {attempts} attempts")
                        raise e
                    
                    sleep_time = base_delay * (2 ** (attempts - 1))
                    if jitter:
                        sleep_time += random.uniform(0, 0.5 * sleep_time)
                    
                    logger.warning(f"Retrying {func.__name__} in {sleep_time:.2f}s...")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

def validate_connection_stability(target_url: str) -> bool:
    """
    Heuristic check to determine if network is suitable for clicking sync.
    Checks for basic DNS and socket resolution overhead.
    """
    import socket
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False