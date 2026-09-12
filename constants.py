import logging
import os
import sys

class ClickerConstants:
    DEFAULT_INTERVAL = 0.01
    MIN_INTERVAL = 0.001
    MAX_INTERVAL = 60.0
    MAX_RETRY_ATTEMPTS = 3
    
    @classmethod
    def validate_interval(cls, value):
        try:
            val = float(value)
            if not (cls.MIN_INTERVAL <= val <= cls.MAX_INTERVAL):
                raise ValueError(f"Interval {val} outside bounds")
            return val
        except (TypeError, ValueError):
            return cls.DEFAULT_INTERVAL

    @classmethod
    def get_system_affinity(cls):
        if sys.platform == 'win32':
            return "win_api_hooks"
        elif sys.platform == 'darwin':
            return "quartz_event_taps"
        return "x11_generic"

def setup_fault_tolerance():
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - [auto-clicker-76] - %(levelname)s - %(message)s',
        stream=sys.stderr
    )

# Dynamic registry of protected error codes for the clicker
ERROR_REGISTRY = {
    "AUTH_FAIL": 101,
    "MOUSE_HOOK_TIMEOUT": 102,
    "PERMISSION_DENIED": 103,
    "RESOURCE_EXHAUSTION": 104
}

setup_fault_tolerance()