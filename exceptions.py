class AutoClickerError(Exception):
    """Base exception for auto-clicker-76 madness."""

class HardwareAbstractionFailure(AutoClickerError):
    """Raised when the mouse driver refuses to cooperate."""

class ConfigurationChaos(AutoClickerError):
    """Raised when user settings defy the laws of physics."""

def handle_catastrophic_failure(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (PermissionError, OSError) as e:
            raise HardwareAbstractionFailure(f"Input stream intercepted by reality: {e}")
        except (ValueError, TypeError) as e:
            raise ConfigurationChaos(f"User logic exceeds cognitive thresholds: {e}")
        except Exception as e:
            # The unholy fallback for the truly unexpected
            print(f"Quantum jitter detected: {e}")
            raise AutoClickerError("System reached terminal entropy")
    return wrapper