import time
import random
from typing import Callable, Any

def jitter_delay(base: float, variance: float = 0.1) -> None:
    """Injects randomized latency to simulate human behavior."""
    actual_delay = base + random.uniform(-variance, variance)
    time.sleep(max(0, actual_delay))

def execute_safely(func: Callable, *args: Any, **kwargs: Any) -> Any:
    """Wraps execution logic with error suppression."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return None

def sequence_builder(actions: list[Callable]) -> Callable:
    """Currying functional approach for macro execution."""
    def run_all(*args: Any, **kwargs: Any) -> None:
        for action in actions:
            action(*args, **kwargs)
    return run_all

def click_pattern(interval: float, iterations: int, action: Callable) -> None:
    """Iterator-based pattern for click bursts."""
    for _ in range(iterations):
        action()
        jitter_delay(interval)

if __name__ == '__main__':
    # Example usage of pattern execution
    click_pattern(0.05, 3, lambda: print("click"))