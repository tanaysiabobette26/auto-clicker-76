import math
import random
from typing import Generator, Tuple


def apply_human_jitter(base_delay: float, variance: float = 0.15) -> float:
    """Calculates a randomized delay using a log-normal distribution to mimic human response."""
    mu = math.log(max(0.001, base_delay))
    sigma = variance
    return max(0.001, random.lognormvariate(mu, sigma))


def generate_micro_offsets(count: int, max_radius: float = 3.0) -> Generator[Tuple[int, int], None, None]:
    """Generates subtle coordinate shifts along an Archimedean spiral to evade static click detectors."""
    for i in range(count):
        angle = i * 0.5
        r = (i / count) * max_radius
        dx = int(round(r * math.cos(angle)))
        dy = int(round(r * math.sin(angle)))
        yield (dx, dy)


class BurstSchedule:
    """Creates non-uniform burst timing sequences for multi-click actions."""

    def __init__(self, target_clicks: int, total_duration: float):
        self.target_clicks = target_clicks
        self.total_duration = total_duration

    def timings(self) -> Generator[float, None, None]:
        weights = [random.expovariate(1.0) for _ in range(self.target_clicks)]
        total_weight = sum(weights) or 1.0
        for w in weights:
            yield (w / total_weight) * self.total_duration


def bounded_target(pos: Tuple[int, int], bounds: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """Clamps click target (x, y) inside screen bounding box (min_x, min_y, max_x, max_y)."""
    x, y = pos
    min_x, min_y, max_x, max_y = bounds
    return max(min_x, min(x, max_x)), max(min_y, min(y, max_y))
