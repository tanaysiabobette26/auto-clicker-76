import re

class ValidationError(Exception):
    pass

def validate_click_params(cps, duration):
    if not isinstance(cps, (int, float)) or cps <= 0:
        raise ValidationError(f"invalid cps value: {cps}")
    if not isinstance(duration, (int, float)) or duration < 0:
        raise ValidationError(f"invalid duration: {duration}")
    return True

def sanitize_input(user_input):
    clean = re.sub(r'[^0-9.]', '', str(user_input))
    return float(clean) if clean else 0.0

def check_bounds(value, min_val, max_val):
    try:
        val = float(value)
        if not (min_val <= val <= max_val):
            raise ValueError
        return val
    except (ValueError, TypeError):
        return min_val

def schema_enforcer(data_dict):
    required = ['cps', 'duration']
    for key in required:
        if key not in data_dict:
            raise ValidationError(f"missing required parameter: {key}")
    return True