import sys

VERSION = "7.6.0"
APP_NAME = "auto-clicker-76"
DEFAULT_CPS = 20.0
MAX_CPS = 1000.0
MIN_DELAY = 0.001
TOGGLE_KEY = "f6"
EXIT_KEY = "f12"
RECORD_KEY = "f8"
PLAY_KEY = "f9"
CONFIG_FILE = "clicker_config.json"
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] (%(name)s): %(message)s"
LOG_LEVEL = "INFO"
PLATFORM = sys.platform
IS_WINDOWS = PLATFORM.startswith("win")
IS_MACOS = PLATFORM == "darwin"
IS_LINUX = PLATFORM.startswith("linux")
MAX_MACRO_EVENTS = 50000
DEFAULT_MOUSE_BUTTON = "left"
SUPPORTED_BUTTONS = {"left", "right", "middle"}
COLOR_ACCENT = "#00ffcc"
COLOR_BG = "#1e1e1e"
COLOR_TEXT = "#ffffff"
FONT_FAMILY = "Consolas"
FONT_SIZE = 10
