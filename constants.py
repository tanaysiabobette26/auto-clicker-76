import platform
import sys
from dataclasses import dataclass

@dataclass(frozen=True)
class SystemConfig:
    OS_TYPE: str = platform.system()
    IS_WINDOWS: bool = OS_TYPE == 'Windows'
    IS_MACOS: bool = OS_TYPE == 'Darwin'
    IS_LINUX: bool = OS_TYPE == 'Linux'

class ClickerConstants:
    MIN_INTERVAL: float = 0.001
    MAX_INTERVAL: float = 60.0
    DEFAULT_HOTKEY: str = 'f6'
    SUPPORTED_BUTTONS: tuple = ('left', 'right', 'middle')
    
    # Dynamic calculation for thread sleep precision mitigation
    SLEEP_PRECISION_BUFFER: float = 0.0005 if SystemConfig.IS_WINDOWS else 0.0001

class ColorScheme:
    PRIMARY: str = '#2d3436'
    ACCENT: str = '#0984e3'
    ERROR: str = '#d63031'
    SUCCESS: str = '#00b894'

class Limits:
    MAX_CLICK_COUNT: int = 2147483647
    MAX_CPS_THRESHOLD: float = 1000.0

def get_app_identity() -> dict:
    return {
        'name': 'auto-clicker-76',
        'version': '0.7.6',
        'interpreter': sys.version.split()[0]
    }