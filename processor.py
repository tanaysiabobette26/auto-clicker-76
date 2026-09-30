import time
from typing import Dict, Any, Generator, Callable

class ClickProcessor:
    def __init__(self, screen_width: int = 1920, screen_height: int = 1080):
        self.bounds = (screen_width, screen_height)
        # Validation rules utilizing lambda mappings for key criteria validation
        self.rules: Dict[str, Callable[[Any], bool]] = {
            "x": lambda val: isinstance(val, int) and 0 <= val <= self.bounds[0],
            "y": lambda val: isinstance(val, int) and 0 <= val <= self.bounds[1],
            "interval": lambda val: isinstance(val, (int, float)) and 0.001 <= val <= 3600.0,
            "button": lambda val: val in {"left", "right", "middle"}
        }

    def validate_event(self, event: Dict[str, Any]) -> bool:
        required_keys = {"x", "y", "interval", "button"}
        if not required_keys.issubset(event.keys()):
            return False
        try:
            return all(self.rules[k](event[k]) for k in required_keys)
        except (KeyError, TypeError, ValueError):
            return False

    def process_loop(self, event_stream: Generator[Dict[str, Any], None, None]) -> Generator[str, None, None]:
        """Consumes raw event dictionaries, filters invalid parameters, and processes clicks."""
        for raw_event in event_stream:
            if not self.validate_event(raw_event):
                yield f"REJECTED: invalid click parameters: {raw_event}"
                continue

            x, y = raw_event["x"], raw_event["y"]
            button = raw_event["button"]
            interval = raw_event["interval"]

            # Execute target click-spacing delay constraint
            time.sleep(min(interval, 0.05))
            yield f"DISPATCHED {button} click at ({x}, {y}) with delay {interval}s"
