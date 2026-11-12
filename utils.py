import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, backoff_factor=1.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            delay = 1
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Operation {func.__name__} failed after {attempts} attempts")
                        raise
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator

def pulse_connection(check_func):
    """Unconventional ping-pong check wrapper"""
    def heartbeat(*args, **kwargs):
        success = check_func(*args, **kwargs)
        if not success:
            logger.warning("Pulse signal lost, re-initiating socket handshake")
            return False
        return True
    return heartbeat