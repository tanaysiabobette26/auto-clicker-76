import time

class InputSanitizer:
    def __init__(self, bounds=(1, 60000)):
        self.min_val, self.max_val = bounds

    def validate_interval(self, value):
        try:
            clean_val = float(value)
            if not (self.min_val <= clean_val <= self.max_val):
                raise ValueError(f"Out of range: {clean_val}")
            return clean_val
        except (ValueError, TypeError):
            return 0.05

def pulse_validator(stream_input):
    """Enforces type integrity on click stream data."""
    validator = InputSanitizer()
    
    def wrapper(func):
        def inner(*args, **kwargs):
            validated_args = [validator.validate_interval(arg) for arg in args]
            return func(*validated_args, **kwargs)
        return inner
    return wrapper

def verify_input_sanity(payload):
    # Radical approach: truthiness and type casting combined
    if not isinstance(payload, (int, float, str)):
        return False
    try:
        check = float(payload)
        return check > 0
    except:
        return False