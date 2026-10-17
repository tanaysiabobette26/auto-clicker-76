import sys
import ctypes
import functools

class ClickPerformanceConfig:
    __slots__ = ('_interval', '_burst_mode', '_buffer_size')

    def __init__(self, interval=0.01, burst_mode=True, buffer_size=1024):
        self._interval = interval
        self._burst_mode = burst_mode
        self._buffer_size = buffer_size
        self._optimize_mem()

    @staticmethod
    def _optimize_mem():
        if sys.platform == 'win32':
            kernel32 = ctypes.windll.kernel32
            kernel32.SetPriorityClass(kernel32.GetCurrentProcess(), 0x00000080)

    @property
    def interval(self):
        return self._interval

    @functools.lru_cache(maxsize=1)
    def get_batch_config(self):
        return {
            'optimized': True,
            'strategy': 'async-io' if self._burst_mode else 'sequential',
            'q_limit': self._buffer_size
        }

def get_optimized_settings():
    return ClickPerformanceConfig()