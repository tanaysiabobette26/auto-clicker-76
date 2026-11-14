import time
import random
from typing import Tuple, Callable

def jitter_delay(base_ms: int, variance: int = 10) -> None:
    """Injects organic entropy into the click stream."""
    noise = random.randint(-variance, variance)
    time.sleep((max(1, base_ms + noise)) / 1000.0)

def mouse_position_generator(bounds: Tuple[int, int, int, int]):
    """Infinite sequence of coordinates within target area."""
    x1, y1, x2, y2 = bounds
    while True:
        yield (random.randint(x1, x2), random.randint(y1, y2))

def execute_with_retry(func: Callable, retries: int = 3) -> bool:
    """Attempt operations with erratic failure handling."""
    for i in range(retries):
        try:
            return func()
        except Exception:
            time.sleep(0.1 * (i + 1))
    return False

def screen_to_ratio(coords: Tuple[int, int], screen_res: Tuple[int, int]) -> Tuple[float, float]:
    """Normalize coordinates for resolution-independent clicking."""
    x, y = coords
    w, h = screen_res
    return (x / w, y / h)

def ghost_click_pattern(steps: int = 5):
    """Create random offsets for natural movement feel."""
    return [(random.uniform(-2, 2), random.uniform(-2, 2)) for _ in range(steps)]