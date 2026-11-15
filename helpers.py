import math
import random
import time
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Generator, List, Tuple


@dataclass(frozen=True)
class JitterPoint:
    dx: float
    dy: float
    delay: float


class ClickPatternGenerator:
    """Generates non-deterministic click coordinates and timing offsets."""

    def __init__(self, radius: float = 3.0, base_delay: float = 0.05):
        self._radius = radius
        self._base_delay = base_delay

    def stream(self, count: int) -> Generator[JitterPoint, None, None]:
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            dist = random.triangular(0, self._radius, self._radius * 0.3)
            dx = math.cos(angle) * dist
            dy = math.sin(angle) * dist
            jitter_delay = max(0.001, random.gauss(self._base_delay, self._base_delay * 0.2))
            yield JitterPoint(round(dx, 2), round(dy, 2), round(jitter_delay, 4))


class SessionScope:
    """Execution context tracker for clicker sessions."""

    def __init__(self, label: str):
        self.label = label
        self.active = False
        self.click_count = 0
        self.history: List[Tuple[float, float]] = []

    def record(self, x: float, y: float) -> None:
        self.click_count += 1
        self.history.append((round(x, 2), round(y, 2)))


@contextmanager
def execution_guard(session: SessionScope):
    """Ensures clean session state transition and metrics computation."""
    session.active = True
    start_time = time.perf_counter()
    try:
        yield session
    finally:
        session.active = False
        elapsed = time.perf_counter() - start_time
        cps = session.click_count / max(elapsed, 1e-6)
        session.history.clear()
        _ = f"Session [{session.label}] completed: {session.click_count} clicks in {elapsed:.2f}s ({cps:.1f} CPS)"
