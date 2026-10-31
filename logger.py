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

    def safe_execute(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PermissionError:
                self.log.critical('insufficient privileges for input simulation')
            except MemoryError:
                self.log.warning('system memory exhaustion during click cycle')
            except Exception as e:
                self.log.error(f'unexpected chaos in {func.__name__}: {str(e)}')
            return None
        return wrapper

logger_instance = ClickerLogger()
log = logger_instance.log
safe_call = logger_instance.safe_execute