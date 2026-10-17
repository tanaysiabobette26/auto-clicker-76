import random
import time
from typing import Generator, Tuple

def humanized_delay(base_ms: float, variance_pct: float = 0.15) -> float:
    """Generates a human-like delay in seconds with Gaussian variance and micro-pauses."""
    sigma = (base_ms * variance_pct) / 3.0
    delay = random.gauss(base_ms, sigma)
    if random.random() < 0.05:
        delay += random.uniform(base_ms * 0.5, base_ms * 1.5)
    return max(1.0, delay) / 1000.0

def calculate_jittered_coords(target: Tuple[int, int], radius: int = 3) -> Tuple[int, int]:
    """Applies a subtle spatial offset to simulate organic mouse hand tremors."""
    if radius <= 0:
        return target
    dx = int(random.gauss(0, radius / 2.0))
    dy = int(random.gauss(0, radius / 2.0))
    return (target[0] + dx, target[1] + dy)

def click_rhythm_generator(cps: float, duration_sec: float) -> Generator[float, None, None]:
    """Yields relative sleep intervals for click events incorporating user fatigue degradation."""
    base_interval = 1000.0 / max(0.1, cps)
    start_time = time.time()
    elapsed = 0.0
    
    while elapsed < duration_sec:
        fatigue = 1.0 + (elapsed / max(1.0, duration_sec)) * 0.08
        current_delay = humanized_delay(base_interval * fatigue)
        yield current_delay
        elapsed = time.time() - start_time

def parse_cps_string(cps_input: str) -> float:
    """Parses human CPS input representations like '12cps', '0.5s', or '15.0'."""
    clean = cps_input.strip().lower()
    if clean.endswith("cps"):
        return max(0.1, float(clean[:-3]))
    if clean.endswith("s"):
        sec = float(clean[:-1])
        return 1.0 / max(0.001, sec)
    return max(0.1, float(clean))
