import time
import pyautogui

class AutoClicker:
    def __init__(self, interval=1, button='left'):
        self.interval = interval
        self.button = button
        self.running = False

    def start(self):
        self.running = True
        print(f'Starting auto-clicker with {self.button} button every {self.interval} seconds.')
        while self.running:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

    def stop(self):
        self.running = False
        print('Auto-clicker stopped.')

    def set_interval(self, interval):
        if interval > 0:
            self.interval = interval
            print(f'Interval set to {self.interval} seconds.')
        else:
            print('Interval must be greater than zero.')

    def set_button(self, button):
        if button in ['left', 'right', 'middle']:
            self.button = button
            print(f'Button set to {self.button}.')
        else:
            print('Invalid button. Please choose left, right, or middle.')

if __name__ == '__main__':
    auto_clicker = AutoClicker(interval=0.5)
    try:
        auto_clicker.start()
    except KeyboardInterrupt:
        auto_clicker.stop()