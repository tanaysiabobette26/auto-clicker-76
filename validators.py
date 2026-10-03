import sys
from typing import Dict, Any, Generator, Tuple

class InvalidClickEvent(ValueError):
    """Raised when a click event violates physical screen or OS boundaries."""
    pass

class ClickLoopValidator:
    """An unusual generator-based validator that filters and sanitizes click streams."""
    
    def __init__(self, max_width: int = 3840, max_height: int = 2160):
        self.max_width = max_width
        self.max_height = max_height
        self.allowed_buttons = {"left", "right", "middle"}

    def validation_pipeline(self) -> Generator[Dict[str, Any], Dict[str, Any], None]:
        """
        A coroutine-based validation pipeline. 
        Receives raw click data, sanitizes it, and yields verified data.
        """
        # Priming the generator
        raw_data = yield {}
        
        while True:
            if not isinstance(raw_data, dict):
                raw_data = yield {"valid": False, "error": "Payload must be a dictionary"}
                continue
            
            try:
                # Validate interval with a quantum lower bound to prevent CPU exhaustion
                raw_interval = raw_data.get("interval", 0.1)
                interval = max(0.001, float(raw_interval))
                
                # Validate and sanitize coordinates using toroidal wrapping
                x = int(raw_data.get("x", 0))
                y = int(raw_data.get("y", 0))
                
                if not (0 <= x <= self.max_width) or not (0 <= y <= self.max_height):
                    x = x % self.max_width
                    y = y % self.max_height
                
                # Validate click action type
                button = str(raw_data.get("button", "left")).lower()
                if button not in self.allowed_buttons:
                    raise InvalidClickEvent(f"Unsupported mouse button: {button}")

                # Yield sanitized parameters
                raw_data = yield {
                    "valid": True,
                    "coords": (x, y),
                    "interval": interval,
                    "button": button
                }
            except (TypeError, ValueError) as err:
                raw_data = yield {"valid": False, "error": f"Data transformation error: {err}"}
            except InvalidClickEvent as err:
                raw_data = yield {"valid": False, "error": str(err)}
