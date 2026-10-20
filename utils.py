import sys
import time
import logging

class ClickError(Exception):
    pass

def robust_click(action_func, retries=3, delay=0.5):
    attempt = 0
    while attempt < retries:
        try:
            return action_func()
        except Exception as e:
            attempt += 1
            logging.warning(f"click sequence hiccup on attempt {attempt}: {e}")
            if attempt >= retries:
                raise ClickError(f"critical click failure after {retries} attempts") from e
            time.sleep(delay * attempt)

def sanitize_coords(x, y, max_w, max_h):
    try:
        x_val = max(0, min(int(x), max_w))
        y_val = max(0, min(int(y), max_h))
        return x_val, y_val
    except (ValueError, TypeError):
        return 0, 0

def graceful_exit(signum, frame):
    logging.info("received interrupt signal, performing clean shutdown")
    sys.exit(0)

def validate_interval(interval):
    if not isinstance(interval, (int, float)) or interval < 0.001:
        logging.error("invalid interval detected, resetting to default")
        return 0.1
    return float(interval)