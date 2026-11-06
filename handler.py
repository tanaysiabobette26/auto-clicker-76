import time
import random
from typing import Callable, Generator, List, Tuple, Optional, TypeVar

T = TypeVar("T")
ClickResult = Tuple[int, float, bool]
ActionCallback = Callable[[ClickResult], None]

class ClickHandler:
    """Dynamic event handler for managing high-frequency click bursts with rhythmic jitter."""

    def __init__(
        self,
        base_interval_ms: float = 50.0,
        jitter_range: Tuple[float, float] = (-5.0, 15.0),
        listeners: Optional[List[ActionCallback]] = None
    ) -> None:
        """Initialize the handler with interval tuning and optional event callbacks."""
        self.base_interval_ms = base_interval_ms
        self.jitter_range = jitter_range
        self.listeners: List[ActionCallback] = listeners or []
        self._sequence_counter: int = 0

    def register_listener(self, callback: ActionCallback) -> None:
        """Attach a subscriber callback to receive click dispatch telemetry."""
        if callback not in self.listeners:
            self.listeners.append(callback)

    def _jitter_generator(self) -> Generator[float, None, None]:
        """Yield continuous variance offsets calculated via non-linear distribution."""
        while True:
            low, high = self.jitter_range
            multiplier = 1.2 if self._sequence_counter % 2 == 0 else 0.8
            yield random.uniform(low, high) * multiplier

    def generate_burst(self, total_clicks: int) -> Generator[ClickResult, None, None]:
        """Execute a controlled burst sequence yielding dispatch metrics per click event.
        
        Args:
            total_clicks: Total number of simulated click iterations to produce.

        Yields:
            ClickResult tuples containing click index, epoch timestamp, and execution flag.
        """
        jitter_stream = self._jitter_generator()

        for _ in range(total_clicks):
            self._sequence_counter += 1
            delay_delta = next(jitter_stream)
            effective_delay = max(1.0, self.base_interval_ms + delay_delta) / 1000.0

            time.sleep(effective_delay)
            event: ClickResult = (self._sequence_counter, time.time(), True)

            for listener in self.listeners:
                listener(event)

            yield event

    def dispatch_matrix(self, click_plan: List[int]) -> List[ClickResult]:
        """Process a batch matrix of burst counts sequentially into a flat telemetry log."""
        log: List[ClickResult] = []
        for burst_size in click_plan:
            log.extend(list(self.generate_burst(burst_size)))
        return log
