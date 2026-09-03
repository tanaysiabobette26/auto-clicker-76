import time
import logging

class ClickProcessor:
    def __init__(self, interval, duration):
        self.interval = interval
        self.duration = duration
        self.is_running = True

    def validate_inputs(self):
        """Sanity check for the clicking parameters."""
        if not isinstance(self.interval, (int, float)) or self.interval < 0.01:
            raise ValueError("Interval must be a positive float >= 0.01s")
        if not isinstance(self.duration, (int, float)) or self.duration <= 0:
            raise ValueError("Duration must be a positive number")

    def process_loop(self):
        try:
            self.validate_inputs()
            start_time = time.time()
            while time.time() - start_time < self.duration:
                if not self.is_running:
                    break
                print(f"Executing click at {time.strftime('%X')}")
                time.sleep(self.interval)
        except ValueError as e:
            logging.error(f"Input validation error: {e}")
        except Exception as e:
            logging.critical(f"Unexpected system disruption: {e}")

if __name__ == "__main__":
    # Example usage for auto-clicker-76
    processor = ClickProcessor(interval=0.5, duration=2.0)
    processor.process_loop()