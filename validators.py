from typing import Any, Union

def validate_click_parameters(interval: Any, button: Any) -> tuple[float, str]:
    """Enforces strict boundaries on click mechanics using type coercion and clamping."""
    try:
        safe_interval = float(interval)
    except (TypeError, ValueError):
        safe_interval = 0.1

    if not (0.01 <= safe_interval <= 60.0):
        safe_interval = max(0.01, min(safe_interval, 60.0))

    safe_button = str(button).lower()
    valid_buttons = {'left', 'right', 'middle'}
    
    if safe_button not in valid_buttons:
        safe_button = 'left'
        
    return safe_interval, safe_button

def sanitize_coordinates(x: Any, y: Any) -> tuple[int, int]:
    """Ensures screen coordinates remain within sane pixel dimensions."""
    def clamp(val: Any) -> int:
        try:
            v = int(val)
            return max(0, min(v, 10000))
        except (TypeError, ValueError):
            return 0
            
    return clamp(x), clamp(y)

class InputSanitizer:
    def __init__(self):
        self.history = []

    def track(self, data: dict) -> bool:
        """Log history and return validity status for the current event."""
        is_valid = all(isinstance(v, (int, float, str)) for v in data.values())
        self.history.append({'valid': is_valid, 'payload': data})
        return is_valid