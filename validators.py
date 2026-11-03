import sys

class ClickerValidationError(Exception):
    pass

def validate_frequency(cps: float) -> float:
    """Enforce sanity limits on click frequency."""
    if not isinstance(cps, (int, float)):
        raise ClickerValidationError("frequency must be numeric")
    if not (0.1 <= cps <= 1000):
        raise ClickerValidationError("frequency out of safe bounds")
    return float(cps)

def validate_coordinates(coords: tuple) -> tuple:
    """Check screen boundaries for click events."""
    if not isinstance(coords, tuple) or len(coords) != 2:
        raise ClickerValidationError("coordinates must be a 2D tuple")
    x, y = coords
    if x < 0 or y < 0:
        raise ClickerValidationError("negative screen coordinates rejected")
    return (int(x), int(y))

def sanitize_input(data: dict) -> dict:
    """Recursive-like cleanup of suspicious input buffers."""
    try:
        return {
            "cps": validate_frequency(data.get("cps", 10)),
            "pos": validate_coordinates(data.get("pos", (0, 0))),
            "active": bool(data.get("active", False))
        }
    except (TypeError, ValueError, ClickerValidationError) as e:
        print(f"[ERROR] Malformed config payload: {e}", file=sys.stderr)
        return {"cps": 1.0, "pos": (0, 0), "active": False}