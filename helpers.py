import math
import random
from typing import Callable, Generator, List, Tuple


class HumanizedInterval:
    """Dynamic timing jitter engine using bell-curve distribution."""

    def __init__(self, base_delay: float, variance: float = 0.15):
        self.base = max(0.001, base_delay)
        self.variance = variance

    def __iter__(self) -> Generator[float, None, None]:
        while True:
            jitter = random.gauss(0, self.variance * self.base)
            delay = max(0.001, self.base + jitter)
            if random.random() < 0.03:
                delay += random.uniform(0.1, 0.35)
            yield delay


class TargetScatter:
    """Calculates realistic click dispersion across a target coordinate."""

    @staticmethod
    def apply_dispersion(
        point: Tuple[int, int], radius: int = 5
    ) -> Tuple[int, int]:
        x, y = point
        angle = random.uniform(0, 2 * math.pi)
        r = radius * math.sqrt(random.random())
        dx = int(round(r * math.cos(angle)))
        dy = int(round(r * math.sin(angle)))
        return (x + dx, y + dy)


def batch_process(
    coords: List[Tuple[int, int]], transform: Callable
) -> Generator[Tuple[int, int], None, None]:
    """Cleans up and yields transformed point coordinates on demand."""
    return (transform(pt) for pt in coords if len(pt) == 2)


def calculate_cps(click_timestamps: List[float]) -> float:
    """Calculates current clicks-per-second rate over a sliding window."""
    if len(click_timestamps) < 2:
        return 0.0
    duration = click_timestamps[-1] - click_timestamps[0]
    return len(click_timestamps) / duration if duration > 0 else 0.0
