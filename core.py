import time
import pyautogui
from dataclasses import dataclass

@dataclass
class ClickerConfig:
    interval: float = 0.1
    button: str = 'left'

class AutoClicker:
    def __init__(self, config: ClickerConfig):
        self.config = config
        self._running = False

    def run(self):
        self._running = True
        try:
            while self._running:
                pyautogui.click(button=self.config.button)
                time.sleep(self.config.interval)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self._running = False

class Orchestrator:
    def __init__(self):
        self.engine = AutoClicker(ClickerConfig())

    def execute_session(self):
        print('Initialization of clicker sequence')
        self.engine.run()

if __name__ == '__main__':
    Orchestrator().execute_session()