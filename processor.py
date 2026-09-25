import pyautogui
import time
import threading

class ClickProcessor:
    def __init__(self, interval=0.1, button='left'):
        self.interval = interval
        self.button = button
        self._running = False

    def _execute_stream(self):
        while self._running:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

    def toggle(self, state: bool):
        if state and not self._running:
            self._running = True
            threading.Thread(target=self._execute_stream, daemon=True).start()
        else:
            self._running = False

    def update_settings(self, interval: float, button: str):
        self.interval = max(0.001, interval)
        self.button = button

def create_processor(config):
    return ClickProcessor(
        interval=config.get('delay', 0.1),
        button=config.get('btn', 'left')
    )