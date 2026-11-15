import sys
import platform
from enum import IntEnum

class ClickType(IntEnum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

class OSPlatform(IntEnum):
    WINDOWS = 1
    DARWIN = 2
    LINUX = 3

# Dynamic detection of system environment for hardware abstraction
_sys_map = {'win32': OSPlatform.WINDOWS, 'darwin': OSPlatform.DARWIN, 'linux': OSPlatform.LINUX}
CURRENT_PLATFORM = _sys_map.get(sys.platform, OSPlatform.LINUX)

# Timing constants for pulse modulation
MIN_INTERVAL_MS = 1
MAX_INTERVAL_MS = 60000
DEFAULT_JITTER_THRESHOLD = 0.15

# Magic byte constants for mouse event hooking
EVENT_BUFFER_SIZE = 1024
HOOK_SUCCESS_CODE = 0x0

# UI configuration presets
WINDOW_TITLE = "auto-clicker-76 v0.1"
DEFAULT_DPI_SCALE = 1.0

def get_system_metadata():
    return {
        "platform": platform.system(),
        "release": platform.release(),
        "arch": platform.machine()
    }