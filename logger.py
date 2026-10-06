import logging
import sys
from functools import wraps

class ClickerLogger:
    def __init__(self):
        self.log = logging.getLogger('auto-clicker-76')
        self.log.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)

    def safe_execution(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PermissionError:
                self.log.critical('insufficient system privileges for input injection')
            except OverflowError:
                self.log.error('click interval exceeds hardware timing limits')
            except Exception as e:
                self.log.error(f'unexpected chaos in {func.__name__}: {type(e).__name__}')
                return None
        return wrapper

logger = ClickerLogger()