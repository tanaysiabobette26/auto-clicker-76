from typing import Any, Dict, Generator, Tuple

class ValidationError(ValueError):
    """Custom exception for invalid click target parameters."""
    pass

def validate_click_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validates and coerces click loop inputs prior to dispatch."""
    validators = {
        "coords": lambda c: isinstance(c, (list, tuple)) and len(c) == 2 and all(isinstance(n, int) and n >= 0 for n in c),
        "delay": lambda d: isinstance(d, (int, float)) and 0.001 <= d <= 3600.0,
        "button": lambda b: str(b).lower() in ("left", "right", "middle"),
        "clicks": lambda n: isinstance(n, int) and 1 <= n <= 10000,
    }
    
    cleaned = {}
    for key, check in validators.items():
        if key not in payload:
            raise ValidationError(f"Missing mandatory payload key: '{key}'")
        val = payload[key]
        if not check(val):
            raise ValidationError(f"Parameter '{key}' failed validation check: {val}")
        cleaned[key] = str(val).lower() if key == "button" else val

    jitter = payload.get("jitter", 0)
    if not (isinstance(jitter, (int, float)) and 0 <= jitter <= 50):
        raise ValidationError(f"Jitter radius out of allowed range [0, 50]: {jitter}")
    cleaned["jitter"] = float(jitter)

    return cleaned

def validate_loop_inputs(input_queue: list) -> Generator[Tuple[bool, dict], None, None]:
    """Yields sanitized inputs or error telemetry for main event stream."""
    for raw_item in input_queue:
        try:
            yield True, validate_click_payload(raw_item)
        except ValidationError as exc:
            yield False, {"error": str(exc), "raw_input": raw_item}
