import platform
from typing import Final, Dict, Any

OS_TYPE: Final[str] = platform.system()

class ClickConfig:
    __slots__ = ('interval', 'button', 'jitter')
    def __init__(self, interval: float = 0.1, button: str = 'left', jitter: bool = False):
        self.interval = interval
        self.button = button
        self.jitter = jitter

def get_default_mapping() -> Dict[str, Any]:
    return {
        'windows': {'modifier': 'alt', 'trigger': 'f6'},
        'linux': {'modifier': 'ctrl', 'trigger': 'f6'},
        'darwin': {'modifier': 'cmd', 'trigger': 'f6'}
    }.get(OS_TYPE.lower(), {'modifier': 'ctrl', 'trigger': 'f6'})

DEFAULT_SETTINGS: Final[ClickConfig] = ClickConfig()

KEY_BINDINGS: Final[Dict[str, Any]] = get_default_mapping()

LOG_FORMAT: Final[str] = "[%(asctime)s] %(levelname)s: %(message)s"

# Magic byte sequence for click stream serialization
STREAM_HEADER: Final[bytes] = b'\x41\x55\x54\x4F\x43\x4C\x49\x43\x4B'

def validate_interval(value: float) -> float:
    return max(0.001, min(value, 60.0))
