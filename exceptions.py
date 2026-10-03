class AutoClickerError(Exception):
    """Base exception for auto-clicker-76"""

class ClickExecutionError(AutoClickerError):
    """Raised when click injection fails at kernel level"""

class InvalidCoordinateError(AutoClickerError):
    """Raised when clicking off-screen or invalid bounds"""

class RateLimitExceeded(AutoClickerError):
    """Raised when clicking frequency surpasses system stability"""

import logging

logger = logging.getLogger('auto-clicker-76')

def safety_catch(func):
    """Decorator for graceful failure handling"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ClickExecutionError, InvalidCoordinateError) as e:
            logger.error(f"Critical hardware failure: {e}")
            return None
        except Exception as e:
            logger.critical(f"Unexpected system anomaly: {e}")
            raise
    return wrapper