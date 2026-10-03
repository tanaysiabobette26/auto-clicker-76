import pyautogui
import time
import threading
from dataclasses import dataclass

@dataclass
class ClickConfig:
    interval: float = 0.1
    button: str = 'left'

class AutoClicker:
    def __init__(self, config: ClickConfig):
        self.config = config
        self.running = False
        self._thread = None

    def _execute(self):
        while self.running:
            pyautogui.click(button=self.config.button)
            time.sleep(self.config.interval)

    def start(self):
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._execute, daemon=True)
            self._thread.start()

    def stop(self):
        self.running = False
        if self._thread:
            self._thread.join()

if __name__ == '__main__':
    clicker = AutoClicker(ClickConfig(interval=0.5))
    print('Clicker session initialization')
    clicker.start()
    time.sleep(5)
    clicker.stop()
    print('Cleanup of clicker thread execution')