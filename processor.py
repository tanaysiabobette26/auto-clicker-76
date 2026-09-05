import time
import logging

class ClickProcessor:
    def __init__(self, interval, clicks):
        self.interval = interval
        self.clicks = clicks

    def _is_sane(self, interval, clicks):
        return isinstance(interval, (int, float)) and interval > 0.01 and \
               isinstance(clicks, int) and 0 < clicks <= 10000

    def run(self):
        if not self._is_sane(self.interval, self.clicks):
            logging.error("invalid configuration detected")
            return

        print(f"starting click stream: {self.clicks} ops at {self.interval}s")
        for i in range(self.clicks):
            try:
                self._perform_click(i)
                time.sleep(self.interval)
            except KeyboardInterrupt:
                print("abort sequence initiated")
                break

    def _perform_click(self, index):
        # simulated click logic
        print(f"[{index+1}] mouse event trigger")

if __name__ == '__main__':
    processor = ClickProcessor(0.5, 10)
    processor.run()