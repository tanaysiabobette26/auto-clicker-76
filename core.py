import math
import random
from typing import Generator, List, Tuple

Point = Tuple[int, int]

class HumanJitter:
    """Generates human-like timing variations using a truncated Gaussian curve."""
    def __init__(self, target_cps: float, variance: float = 0.2):
        self.base_delay = 1.0 / max(0.1, target_cps)
        self.variance = variance

    def __iter__(self):
        return self

    def __next__(self) -> float:
        delay = random.gauss(self.base_delay, self.base_delay * self.variance)
        return max(0.001, delay)

def generate_bezier_path(start: Point, end: Point, control_points_count: int = 2, steps: int = 20) -> List[Point]:
    """Calculates an n-point Bezier curve path to mimic human mouse movement."""
    def binomial(n: int, k: int) -> int:
        return math.comb(n, k)

    controls = [start]
    for i in range(1, control_points_count + 1):
        ratio = i / (control_points_count + 1)
        mid_x = start[0] + (end[0] - start[0]) * ratio
        mid_y = start[1] + (end[1] - start[1]) * ratio
        offset_x = random.randint(-40, 40)
        offset_y = random.randint(-40, 40)
        controls.append((int(mid_x + offset_x), int(mid_y + offset_y)))
    controls.append(end)

    n = len(controls) - 1
    path = []
    for step in range(steps + 1):
        t = step / steps
        x, y = 0.0, 0.0
        for i, p in enumerate(controls):
            coeff = binomial(n, i) * ((1 - t) ** (n - i)) * (t ** i)
            x += coeff * p[0]
            y += coeff * p[1]
        path.append((int(round(x)), int(round(y))))
    return path

def calculate_burst_schedule(total_clicks: int, target_duration: float) -> Generator[float, None, None]:
    """Yields precise sleep intervals distributed evenly with micro-burst perturbations."""
    base_interval = target_duration / max(1, total_clicks)
    accumulated_drift = 0.0
    
    for _ in range(total_clicks):
        noise = random.uniform(-0.15, 0.15) * base_interval
        scheduled = base_interval + noise - accumulated_drift
        actual_delay = max(0.0005, scheduled)
        accumulated_drift = actual_delay - base_interval
        yield round(actual_delay, 5)
