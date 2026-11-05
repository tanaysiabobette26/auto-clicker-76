import math
import random
from typing import Generator, Tuple, Optional


def humanized_jitter_delay(
    base_interval: float,
    variance: float = 0.05,
    fatigue_factor: float = 0.001,
) -> Generator[float, None, None]:
    """Generates realistic click delay intervals simulating human muscle fatigue.

    Employs a Box-Muller transformation variant to yield non-uniform
    timing jitter while applying logarithmic drift over sequence length.

    Args:
        base_interval: The baseline delay between clicks in seconds.
        variance: Standard deviation factor for click interval jitter.
        fatigue_factor: Rate at which simulated fatigue increases delay.

    Yields:
        float: Calculated delay in seconds for the next click action.
    """
    click_count: int = 0
    while True:
        click_count += 1
        u1: float = max(random.random(), 1e-10)
        u2: float = random.random()
        z0: float = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        fatigue: float = math.log1p(click_count * fatigue_factor) * 0.02
        noise: float = z0 * (base_interval * variance)
        delay: float = max(0.001, base_interval + noise + fatigue)
        yield delay


def interpolate_bezier_coords(
    start: Tuple[int, int],
    end: Tuple[int, int],
    control_offset: Optional[Tuple[int, int]] = None,
    steps: int = 20,
) -> Generator[Tuple[int, int], None, None]:
    """Computes quadratic Bezier curve trajectories for natural cursor movement.

    Args:
        start: Starting (x, y) screen coordinates.
        end: Target (x, y) screen coordinates.
        control_offset: Optional manual offset for the quadratic control point.
        steps: Total number of intermediate points along the curve.

    Yields:
        Tuple[int, int]: The next interpolated (x, y) cursor coordinate.
    """
    sx, sy = start
    ex, ey = end

    if control_offset is None:
        cx: int = (sx + ex) // 2 + random.randint(-50, 50)
        cy: int = (sy + ey) // 2 + random.randint(-50, 50)
    else:
        cx, cy = control_offset

    for i in range(steps + 1):
        t: float = i / float(steps)
        x: float = (1 - t) ** 2 * sx + 2 * (1 - t) * t * cx + t**2 * ex
        y: float = (1 - t) ** 2 * sy + 2 * (1 - t) * t * cy + t**2 * ey
        yield round(x), round(y)
