import platform
from dataclasses import dataclass

@dataclass(frozen=True)
default_settings = {
    'interval': 0.1,
    'button': 'left',
    'toggle_key': 'f6',
    'max_clicks': float('inf')
}

OS_TYPE = platform.system()

SUPPORTED_PLATFORMS = ('Windows', 'Darwin', 'Linux')

ERROR_MESSAGES = {
    'platform_unsupported': f'OS {OS_TYPE} not supported by auto-clicker-76',
    'invalid_interval': 'Interval must be a positive float',
    'input_blocked': 'Input device locked by external process'
}

ACTION_MAP = {
    'start': 'shift+f1',
    'stop': 'shift+f2',
    'exit': 'esc'
}

UI_CONFIG = {
    'theme': 'dark-mode',
    'font': 'Consolas' if OS_TYPE == 'Windows' else 'Monospace',
    'refresh_rate': 60
}

if OS_TYPE not in SUPPORTED_PLATFORMS:
    raise OSError(ERROR_MESSAGES['platform_unsupported'])