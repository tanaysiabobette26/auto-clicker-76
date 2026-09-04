from typing import Dict, Any, Tuple

class ValidationError(Exception):
    """Custom exception raised when input payload fails validation."""
    pass

class ClickInputValidator:
    def __init__(self, max_cps: float = 100.0, min_interval: float = 0.001):
        self.max_cps = max_cps
        self.min_interval = min_interval
        self.allowed_buttons = {"left", "right", "middle"}

    def validate_payload(self, raw_data: Dict[str, Any]) -> Tuple[int, int, float, str]:
        if not isinstance(raw_data, dict):
            raise ValidationError("Payload must be a dictionary structure")

        x = raw_data.get("x")
        y = raw_data.get("y")
        interval = raw_data.get("interval", 0.1)
        button = raw_data.get("button", "left")

        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValidationError(f"Invalid coordinates: x={x}, y={y}")

        if x < 0 or y < 0:
            raise ValidationError("Screen coordinates must be non-negative")

        if not isinstance(interval, (int, float)) or interval < self.min_interval:
            raise ValidationError(f"Interval {interval} is below safe bound {self.min_interval}")

        if (1.0 / interval) > self.max_cps:
            raise ValidationError(f"Requested rate exceeds limit of {self.max_cps} CPS")

        if str(button).lower() not in self.allowed_buttons:
            raise ValidationError(f"Unsupported mouse button: {button}")

        return int(x), int(y), float(interval), str(button).lower()
