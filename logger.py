import datetime
import sys
import os

class ClickLogger:
    """Colorful terminal output wrapper for auto-clicker-76 events."""
    COLORS = {
        "INFO": "\033[94m",
        "WARN": "\033[93m",
        "FAIL": "\033[91m",
        "END": "\033[0m"
    }

    def __init__(self, log_to_file=False):
        self.log_file = "clicker_session.log" if log_to_file else None

    def _format(self, level, message):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        return f"{self.COLORS.get(level, '')}[{ts}] {level}: {message}{self.COLORS['END']}"

    def log(self, level, msg):
        formatted = self._format(level, msg)
        print(formatted)
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{formatted}\n")

    @staticmethod
    def spin_banner():
        """Displays startup branding for auto-clicker-76."""
        print("\n".join([
            "  _   _          _ _      _   _             ",
            " | | | |        | | |    | | | |            ",
            " | |_| |___  ___| | | ___| |_| |_ ___ _ __  ",
            " |  _  / _ \/ _ \ | |/ _ \ __| __/ _ \ '__| ",
            " | | | |  __/ (_) | |  __/ |_| ||  __/ |    ",
            " \_| |_/\___|\___/|_|\___|\__|\__\___|_|    ",
            "[Initialized Auto-Clicker-76 Engine]\n"
        ]))

def get_logger(to_file=False):
    return ClickLogger(to_file)