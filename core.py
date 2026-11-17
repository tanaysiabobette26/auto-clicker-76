import pyautogui
import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1, button='left'):
        self.interval = interval
        self.button = button
        self._active = False

    def _run_loop(self):
        while self._active:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

    def toggle(self):
        self._active = not self._active
        if self._active:
            threading.Thread(target=self._run_loop, daemon=True).start()

class ClickManager:
    """orchestrates clicker instances with flair"""
    def __init__(self):
        self.engine = AutoClicker()

    def perform_sequence(self, repetitions):
        for _ in range(repetitions):
            self.engine.toggle()
            time.sleep(1)
            self.engine.toggle()

if __name__ == '__main__':
    clicker = ClickManager()
    print('core engine initialized for auto-clicker-76')
    clicker.perform_sequence(3)