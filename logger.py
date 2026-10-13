import datetime
import sys

class ClickLogger:
    def __init__(self, log_file: str = "clicker.log"):
        self.log_file = log_file
        self._header = "[AUTO-CLICKER-76 STATUS]"

    def _format(self, level: str, message: str) -> str:
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{ts} | {level:^7} | {message}"

    def log(self, message: str, level: str = "INFO"):
        formatted = self._format(level, message)
        print(formatted)
        try:
            with open(self.log_file, "a") as f:
                f.write(formatted + "\n")
        except IOError:
            print(self._format("ERROR", "Unable to write to log file"))

    def critical(self, message: str):
        self.log(message, "CRIT")
        sys.exit(1)

    def __enter__(self):
        self.log("Session started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.log(f"Crash encountered: {exc_val}", "FATAL")
        else:
            self.log("Session closed cleanly")
