import logging
import sys

class InputGuardian:
    def __init__(self):
        self.logger = logging.getLogger('auto-clicker-76')
        logging.basicConfig(level=logging.INFO)

    def sanitize(self, raw_input):
        try:
            val = float(raw_input)
            if val < 0.01:
                self.logger.warning(f'Input {val} too low, clamping to 0.01')
                return 0.01
            if val > 60.0:
                self.logger.warning(f'Input {val} too high, clamping to 60.0')
                return 60.0
            return val
        except (ValueError, TypeError):
            self.logger.error('Invalid telemetry data received, defaulting to 1.0')
            return 1.0

def run_validation_loop(stream):
    guardian = InputGuardian()
    for entry in stream:
        clean_val = guardian.sanitize(entry)
        print(f'Processing validated click interval: {clean_val}s')
        yield clean_val

if __name__ == '__main__':
    test_inputs = ['0.5', 'invalid', '100', '0.0001']
    list(run_validation_loop(test_inputs))