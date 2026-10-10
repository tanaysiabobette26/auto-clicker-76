import time
import pyautogui

def validate_inputs(interval, duration):
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError('interval must be float >= 0.01')
    if not isinstance(duration, (int, float)) or duration <= 0:
        raise ValueError('duration must be positive number')
    return True

def start_clicking(interval, duration):
    try:
        validate_inputs(interval, duration)
        print(f'Initiating clicks: {interval}s interval for {duration}s')
        end_time = time.time() + duration
        while time.time() < end_time:
            pyautogui.click()
            time.sleep(interval)
    except ValueError as e:
        print(f'Configuration anomaly detected: {e}')
    except Exception as e:
        print(f'Unexpected system disruption: {e}')

if __name__ == '__main__':
    # Example of sanitized click configuration
    start_clicking(0.5, 5.0)