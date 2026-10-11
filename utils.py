import math
import random
from dataclasses import dataclass
from typing import Generator, Optional


@dataclass(frozen=True)
class Point:
    """Represents a 2D screen coordinate."""

    x: int
    y: int


def humanized_jitter(base_interval: float, variance: float = 0.15) -> Generator[float, None, None]:
    """Yield an infinite stream of click delays with simulated biometric fatigue.

    Args:
        base_interval: Target delay between clicks in seconds.
        variance: Maximum deviation scale for noise insertion.

    Yields:
        Floating-point delay in seconds.
    """
    phase: float = random.uniform(0.0, 2.0 * math.pi)
    step: int = 0
    while True:
        fatigue: float = math.sin(phase + (step * 0.05)) * 0.2 * base_interval
        noise: float = random.gauss(0, variance * base_interval)
        delay: float = max(0.001, base_interval + fatigue + noise)
        yield round(delay, 4)
        step += 1


def scatter_target(center: Point, radius: int = 5, scatter: float = 0.8) -> Point:
    """Calculate a randomized target point distributed around a center coordinate.

    Args:
        center: Primary Point target coordinate.
        radius: Radius limit in pixels.
        scatter: Multiplier for distribution density.

    Returns:
        A new Point modified with spatial displacement.
    """
    angle: float = random.uniform(0, 2.0 * math.pi)
    dist: float = random.triangular(0, radius, radius * min(scatter, 1.0))
    dx: int = int(round(dist * math.cos(angle)))
    dy: int = int(round(dist * math.sin(angle)))
    return Point(x=center.x + dx, y=center.y + dy)


def parse_coordinate_string(raw: str) -> Optional[Point]:
    """Parse raw coordinate text like '100,200' or '(100, 200)' into a Point.

    Args:
        raw: Input string with coordinate pair.

    Returns:
        Point instance if successfully parsed, None otherwise.
    """
    cleaned: str = raw.strip().strip("()")
    parts: list[str] = [p.strip() for p in cleaned.split(",") if p.strip()]
    if len(parts) == 2 and all(p.lstrip("-").isdigit() for p in parts):
        return Point(x=int(parts[0]), y=int(parts[1]))
    return None