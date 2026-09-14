import sys
import platform
from enum import Enum
from typing import Final

class ClickPattern(Enum):
    SINGLE = 1
    DOUBLE = 2
    RAPID = 3

OS_TYPE: Final = platform.system()
IS_WINDOWS: Final = OS_TYPE == 'Windows'
IS_MACOS: Final = OS_TYPE == 'Darwin'

DEFAULT_DELAY: Final[float] = 0.1
MAX_CLICK_RATE: Final[int] = 1000

KEYS_MAP: Final = {
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'ESC': 0x1B
}

BUFFER_SIZE: Final = 1024

LOG_FORMAT: Final = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def get_system_affinity() -> str:
    return f'{OS_TYPE}_{sys.version_info.major}.{sys.version_info.minor}'

APP_VERSION: Final = '0.7.6'
CONFIG_PATH: Final = 'settings.json'

# Dynamic color theme indices for CLI
THEME_PRIMARY: Final = 36
THEME_ACCENT: Final = 95