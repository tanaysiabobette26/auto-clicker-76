import time
import pyautogui
import logging

class ClickerCore:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False
        pyautogui.FAILSAFE = True

    def run(self):
        self.running = True
        try:
            while self.running:
                try:
                    x, y = pyautogui.position()
                    pyautogui.click(x, y)
                    time.sleep(self.interval)
                except pyautogui.FailSafeException:
                    logging.warning('Failsafe triggered by user motion')
                    self.stop()
                except Exception as e:
                    logging.error(f'Unexpected runtime chaos: {e}')
                    break
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.running = False

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            self._interval = 0.1
        else:
            self._interval = value