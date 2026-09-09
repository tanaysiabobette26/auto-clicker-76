import time
import functools
from typing import Callable, Any, Type

def retry_network_call(retries: int = 3, delay: float = 1.5, exceptions: tuple = (ConnectionError, TimeoutError)):
    """Decorator injecting stubborn execution resilience into network operations."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_err = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_err = e
                    sleep_duration = delay * (2 ** attempt)
                    time.sleep(sleep_duration)
            raise last_err
        return wrapper
    return decorator

def pulse_connection(endpoint: str, timeout: int = 5) -> bool:
    """Simulated connectivity check for clicker synchronization."""
    import socket
    try:
        with socket.create_connection((endpoint, 80), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

@retry_network_call(retries=5, delay=1.0)
def sync_click_server(data: dict):
    """Network synchronization with automatic retry enforcement."""
    if not pulse_connection("clicker.server.internal"):
        raise ConnectionError("Server unreachable")
    return {"status": "success", "payload": data}