import time
import random
from typing import Iterator, Tuple, Callable, TypeVar, Optional

T = TypeVar("T")

class HumanJitterGenerator:
    """Generates deterministic pseudo-chaotic delays to mimic human clicking patterns.
    
    Uses a modified logistic map equation (x_{n+1} = r * x_n * (1 - x_n)) 
    blended with Gaussian noise to bypass basic anti-cheat click detection.
    """

    def __init__(self, base_interval: float, chaos_factor: float = 3.8) -> None:
        self.base_interval: float = base_interval
        self.r: float = chaos_factor
        self.state: float = random.uniform(0.1, 0.9)

    def next_delay(self) -> float:
        """Calculates the next delay in seconds using chaotic attractor math."""
        self.state = self.r * self.state * (1.0 - self.state)
        jitter: float = (self.state - 0.5) * 0.2 * self.base_interval
        noise: float = random.gauss(0, self.base_interval * 0.05)
        return max(0.001, self.base_interval + jitter + noise)


def paced_clicks(
    total_clicks: int, 
    interval: float, 
    jitter_engine: Optional[HumanJitterGenerator] = None
) -> Iterator[Tuple[int, float]]:
    """Yields click index and sleep duration sequence for execution loops.
    
    Args:
        total_clicks: Total number of clicks requested (0 for infinite sequence).
        interval: Target delay between clicks in seconds.
        jitter_engine: Optional jitter generator for anti-pattern timing.
        
    Yields:
        Tuples of (current_click_count, calculated_sleep_duration).
    """
    engine: HumanJitterGenerator = jitter_engine or HumanJitterGenerator(interval)
    count: int = 0
    
    while total_clicks <= 0 or count < total_clicks:
        count += 1
        delay: float = engine.next_delay() if interval > 0 else 0.0
        yield count, delay


def execute_with_drift(
    click_func: Callable[[], T], 
    coords: Tuple[int, int], 
    radius: int = 3
) -> Tuple[T, Tuple[int, int]]:
    """Executes a target function with randomized pixel coordinate drift.
    
    Args:
        click_func: Callable execution target.
        coords: Base (x, y) coordinates for target position.
        radius: Maximum pixel offset from center point.
        
    Returns:
        Tuple containing function result and actual drifted (x, y) targeted.
    """
    dx: int = random.randint(-radius, radius)
    dy: int = random.randint(-radius, radius)
    actual_pos: Tuple[int, int] = (coords[0] + dx, coords[1] + dy)
    res: T = click_func()
    return res, actual_pos