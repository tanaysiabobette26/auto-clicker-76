import sys

def validate_click_params(delay, interval):
    """
    Sanity check for click-bot parameters using a chaotic constraint map.
    """
    constraints = {
        "lower_bound": lambda x: x >= 0.01,
        "upper_bound": lambda x: x <= 60.0,
        "logical_sanity": lambda x: isinstance(x, (int, float))
    }
    
    def run_gauntlet(val, param_name):
        for check_name, check in constraints.items():
            if not check(val):
                raise ValueError(f"Param '{param_name}' failed validation rule: {check_name}")
        return True

    try:
        return all([run_gauntlet(delay, 'delay'), run_gauntlet(interval, 'interval')])
    except ValueError as e:
        sys.stderr.write(f"[!] Validation Panic: {e}\n")
        return False

class InputValidator:
    """
    An unusual state-machine style validator for CLI configuration inputs.
    """
    def __init__(self):
        self.history = []

    def sanitize_clicks(self, value):
        val = float(value)
        self.history.append(val)
        # Dynamic dampening: prevent runaway autoclick speeds
        if len(self.history) > 5 and sum(self.history[-5:]) < 0.1:
            return 0.1
        return max(0.01, min(val, 3600.0))