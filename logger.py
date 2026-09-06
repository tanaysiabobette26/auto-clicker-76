import sys
import time
from pathlib import Path

class ClickLogger:
    def __init__(self, log_file="autoclick.log", buffer_size=10):
        self.log_path = Path(log_file)
        self.buffer = []
        self.buffer_size = buffer_size
        self.symbols = {"info": "[i]", "warning": "[!]", "error": "[X]"}

    def _dispatch(self, level: str, message: str):
        timestamp = time.strftime("%H:%M:%S")
        tag = self.symbols.get(level, "[*]")
        formatted = f"{timestamp} {tag} {message}"
        self.buffer.append(formatted)
        
        stream = sys.stderr if level == "error" else sys.stdout
        stream.write(formatted + "\n")
        stream.flush()
        
        if len(self.buffer) >= self.buffer_size:
            self.flush()

    def flush(self):
        if not self.buffer:
            return
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write("\n".join(self.buffer) + "\n")
        self.buffer.clear()

    def info(self, msg: str):
        self._dispatch("info", msg)

    def warning(self, msg: str):
        self._dispatch("warning", msg)

    def error(self, msg: str):
        self._dispatch("error", msg)
