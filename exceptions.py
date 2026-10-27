class AutoClickerError(Exception):
    """Base exception for the auto-clicker-76 suite."""

class ClickerInterrupt(AutoClickerError):
    """Raised when the user triggers a forced stop."""

class ConfigurationRegistryError(AutoClickerError):
    """Raised when configuration values violate constraints."""

class HardwareAbstractionError(AutoClickerError):
    """Raised during mouse or keyboard event failures."""

def raise_if_none(value: any, context: str) -> None:
    if value is None:
        raise AutoClickerError(f"Null pointer encountered in {context}")

def capture_execution_context(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[!] Critical failure in {func.__name__}: {str(e)}")
            raise AutoClickerError("Kernel-level event processing failure") from e
    return wrapper

def validate_bounds(val: int, min_v: int, max_v: int, name: str):
    if not (min_v <= val <= max_v):
        raise ConfigurationRegistryError(f"{name} out of bounds: {val}")
