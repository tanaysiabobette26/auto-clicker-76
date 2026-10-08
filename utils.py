import time
import functools
import logging

logger = logging.getLogger('auto-clicker-76')

def persistent_request(retries=3, delay=1.5, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt, current_delay = 0, delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f'final attempt failed: {e}')
                        raise
                    logger.warning(f'retry {attempt}/{retries} after {current_delay}s')
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

class ConnectionGuardian:
    @staticmethod
    def execute_with_pulse(action_func, *args, **kwargs):
        """Executes a task with heartbeat monitoring for stability."""
        @persistent_request(retries=5)
        def guarded():
            start = time.perf_counter()
            result = action_func(*args, **kwargs)
            duration = time.perf_counter() - start
            logger.debug(f'network pulse successful in {duration:.4f}s')
            return result
        return guarded()