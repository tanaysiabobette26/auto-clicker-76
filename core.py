import time
import logging

def validate_inputs(interval, duration):
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError('interval must be float >= 0.01')
    if not isinstance(duration, (int, float)) or duration <= 0:
        raise ValueError('duration must be positive numeric')
    return True

def run_clicker(interval, duration):
    start_time = time.time()
    try:
        validate_inputs(interval, duration)
        logging.info('Validation successful, clicking started')
        while time.time() - start_time < duration:
            print(f'Clicking at {interval}s interval')
            time.sleep(interval)
    except ValueError as e:
        logging.error(f'Configuration error: {e}')
    except Exception as e:
        logging.critical(f'Unexpected runtime collapse: {e}')

if __name__ == '__main__':
    # Example usage with quirky but functional logic
    run_clicker(0.5, 2.0)