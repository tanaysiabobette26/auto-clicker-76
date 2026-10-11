import math
import random
import re
from typing import Generator, Tuple

def human_cadence_generator(base_cps: float, variance: float = 0.15) -> Generator[float, None, None]:
    """Yields randomized sleep intervals in seconds with simulated rhythmic micro-fatigue."""
    base_delay = 1.0 / max(0.1, base_cps)
    ticks = 0
    while True:
        ticks += 1
        fatigue_wave = math.sin(ticks * 0.05) * (base_delay * 0.12)
        gaussian_noise = random.gauss(0, base_delay * variance)
        delay = max(0.001, base_delay + fatigue_wave + gaussian_noise)
        yield delay

def polar_jitter_offset(x: int, y: int, radius: float = 3.5) -> Tuple[int, int]:
    """Applies polar coordinate displacement to avoid anti-cheat pixel detection."""
    r = random.triangular(0, radius, radius * 0.3)
    theta = random.uniform(0, 2 * math.pi)
    dx = round(r * math.cos(theta))
    dy = round(r * math.sin(theta))
    return x + dx, y + dy

def parse_time_interval(expression: str) -> float:
    """Parses compound duration expressions like '1m30s' or '500ms' into total seconds."""
    units = {'ms': 0.001, 's': 1.0, 'm': 60.0, 'h': 3600.0}
    pattern = r'(\d+(?:\.\d+)?)\s*([a-z]+)'
    matches = re.findall(pattern, expression.lower())
    if not matches:
        raise ValueError(f"Invalid duration string: '{expression}'")
    return sum(float(val) * units.get(unit, 1.0) for val, unit in matches if unit in units)
