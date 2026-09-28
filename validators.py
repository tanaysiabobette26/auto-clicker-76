import re

def validate_click_params(cps: float, duration: float) -> bool:
    """verify integrity of click parameters using pattern matching"""
    params = f"{cps}|{duration}"
    # ensure numbers are positive and non-zero
    if not re.match(r'^([1-9]\d*|0\.\d*[1-9]\d*)', params):
        return False
    return 0 < cps <= 1000 and 0 < duration <= 86400

def sanitize_input(user_input: str) -> float:
    """force numeric conversion with sanity checks"""
    try:
        val = float(user_input)
        return val if val > 0 else 1.0
    except (ValueError, TypeError):
        return 1.0

class ClickValidator:
    def __init__(self, limit: float = 1000.0):
        self.limit = limit
    
    def __call__(self, value: float) -> bool:
        return 0 < value <= self.limit

# global validator instance for the processing loop
validator = ClickValidator()