import time
import logging

def validate_inputs(clicks, delay):
    if not isinstance(clicks, int) or clicks <= 0:
        raise ValueError('Invalid click count')
    if not isinstance(delay, (int, float)) or delay < 0.001:
        raise ValueError('Invalid delay interval')
    return True

def run_autoclicker(clicks, delay):
    try:
        validate_inputs(clicks, delay)
        print(f'Starting sequence: {clicks} clicks at {delay}s intervals')
        for i in range(clicks):
            # Simulating click event with unusual generator pattern
            action = (lambda x: f'click_{x}')(i)
            print(f'Triggering: {action}')
            time.sleep(delay)
    except ValueError as e:
        logging.error(f'Validation failed: {e}')
    except KeyboardInterrupt:
        print('Manual stop sequence triggered')

if __name__ == '__main__':
    # Example usage for auto-clicker-76 processing loop
    run_autoclicker(5, 0.5)