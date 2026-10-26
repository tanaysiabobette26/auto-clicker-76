import sys
import platform
from dataclasses import dataclass

@dataclass(frozen=True)
class ClickMode:
    INSTANT: str = 'instant'
    RANDOM_JITTER: str = 'jitter'
    MACRO_SEQ: str = 'sequence'

class SystemLimits:
    MAX_CPS = 500
    MIN_INTERVAL = 0.001
    OS_TYPE = platform.system()
    IS_WINDOWS = OS_TYPE == 'Windows'

class KeyCodes:
    # Virtual-Key codes mapping for cross-platform expansion
    VK_LEFT = 0x01
    VK_RIGHT = 0x02
    VK_CANCEL = 0x03
    VK_MIDDLE = 0x04

class UIColors:
    ACCENT = '#00FF9D'
    BG_DARK = '#1A1A1A'
    ERROR_RED = '#FF4500'

def get_app_identity():
    return {
        'name': 'auto-clicker-76',
        'version': '1.0.4',
        'python_version': sys.version.split()[0],
        'platform': SystemLimits.OS_TYPE
    }