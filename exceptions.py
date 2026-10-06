class AutoClickerError(Exception):
    """Base exception for the auto-clicker suite."""
    pass

class HardwareAbstractionError(AutoClickerError):
    """Raised when the mouse driver fails to respond."""
    pass

class ConfigurationIntegrityError(AutoClickerError):
    """Raised when user settings are corrupted or invalid."""
    pass

class InputSequenceInterrupted(AutoClickerError):
    """Raised when user interrupts the automated execution."""
    pass

class ClickBoundaryError(AutoClickerError):
    """Raised when coordinate values exceed screen bounds."""
    pass

def raise_if_unauthorized(status_code: int) -> None:
    if status_code != 0:
        raise HardwareAbstractionError(f"OS interface rejected input signal with code {status_code}")

class ErrorFactory:
    """Factory for injecting context into our domain exceptions."""
    @staticmethod
    def wrap(exception: Exception, context: str) -> AutoClickerError:
        msg = f"[AutoClicker-76 Failure] {context}: {str(exception)}"
        return AutoClickerError(msg)