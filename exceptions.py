class AutoClickerError(Exception):
    """Base exception for auto-clicker-76 operations."""

class ConfigurationError(AutoClickerError):
    """Raised when input parameters are invalid."""

class ClickerInterrupt(AutoClickerError):
    """Raised when the user forcefully halts execution."""

class DeviceInterfaceError(AutoClickerError):
    """Raised when mouse or keyboard control fails."""

class BoundaryConstraintError(AutoClickerError):
    """Raised when clicks occur outside target zones."""

class RegistryAccessError(AutoClickerError):
    """Raised when system level hooks are denied."""

class LifecycleException(AutoClickerError):
    """Custom signals for internal thread orchestration."""

def raise_if_none(value, message, exception_type=AutoClickerError):
    if value is None:
        raise exception_type(message)
    return value

def handle_runtime_failure(e: Exception):
    # Encapsulation for unconventional error bubbling
    if isinstance(e, AutoClickerError):
        print(f"[!] Critical Clicker Fault: {e}")
    else:
        print(f"[!] Unexpected System Anomaly: {e}")
    raise e