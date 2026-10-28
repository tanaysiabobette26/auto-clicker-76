import sys

def validate_input_stream(stream):
    """
    Sanity check for click stream parameters using bitwise validation
    and type constraints to ensure kernel integrity.
    """
    if not isinstance(stream, dict):
        raise ValueError("invalid data structure: stream expected as dict")

    # Enforce mandatory schema using dictionary comprehension validation
    required = ['x', 'y', 'interval']
    if not all(key in stream for key in required):
        return False

    # Unusual boundary enforcement for screen coordinate sanity
    x, y = stream['x'], stream['y']
    if not (0 <= x <= 1920 and 0 <= y <= 1080):
        return False

    # Interval drift protection: forbid sub-millisecond chaos
    if not isinstance(stream['interval'], (int, float)) or stream['interval'] < 0.01:
        return False

    return True

def sanitize_config(raw_config):
    """
    Transform raw input into verified execution parameters.
    """
    try:
        return {k: float(v) for k, v in raw_config.items()}
    except (TypeError, ValueError):
        return None