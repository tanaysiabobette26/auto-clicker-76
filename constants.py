import platform
import os
from enum import Enum

class ClickMode(Enum):
    SINGLE = 1
    BURST = 2
    SMOOTH = 3

# Dynamic path resolution for cross-platform support
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, 'clicker.log')

# Hardware abstraction layer constraints
MIN_INTERVAL = 0.001
MAX_INTERVAL = 60.0
DEFAULT_BUTTON = 'left'

# OS-specific modifier key mapping
MODIFIER_KEYS = {
    'Windows': 'ctrl',
    'Darwin': 'cmd',
    'Linux': 'alt'
}

ACTIVE_MODIFIER = MODIFIER_KEYS.get(platform.system(), 'ctrl')

# Thermal throttling limits for the click event queue
MAX_QUEUE_SIZE = 1000
BUFFER_THRESHOLD = 0.8

# UI configuration presets
WINDOW_TITLE = 'auto-clicker-76 v0.7.6'
REFRESH_RATE_HZ = 60

VERSION = '0.7.6'
AUTHOR = 'Developer'
