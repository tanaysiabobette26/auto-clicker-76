import json
import time
from typing import List, Dict, Any, Generator


class ClickDataProcessor:
    """Processes click event streams with delta-encoding and jitter normalization."""

    def __init__(self, jitter_threshold_ms: float = 2.0):
        self.jitter_threshold = jitter_threshold_ms / 1000.0

    def compress_stream(self, events: List[Dict[str, Any]]) -> List[tuple]:
        """Compresses raw click events into optimized delta-encoded tuples."""
        if not events:
            return []

        compressed = []
        prev_time = events[0].get("timestamp", time.time())

        for event in events:
            curr_time = event.get("timestamp", time.time())
            raw_dt = curr_time - prev_time
            dt = 0.0 if raw_dt < self.jitter_threshold else round(raw_dt, 4)

            x, y = event.get("x", 0), event.get("y", 0)
            btn = event.get("button", "left")[0].lower()
            action = 1 if event.get("pressed", True) else 0

            compressed.append((x, y, dt, btn, action))
            prev_time = curr_time

        return compressed

    def decompress_stream(self, compressed: List[tuple]) -> Generator[Dict[str, Any], None, None]:
        """Reconstructs timed click stream yielders from delta sequence."""
        accumulated_time = time.time()
        btn_map = {'l': 'left', 'r': 'right', 'm': 'middle'}

        for x, y, dt, btn_code, action_code in compressed:
            accumulated_time += dt
            yield {
                "x": int(x),
                "x_rel": x / 1920.0,
                "y": int(y),
                "y_rel": y / 1080.0,
                "delay": dt,
                "timestamp": round(accumulated_time, 4),
                "button": btn_map.get(btn_code, 'left'),
                "pressed": bool(action_code)
            }

    def serialize_profile(self, name: str, compressed_events: List[tuple]) -> str:
        """Packages sequence into compact JSON profile payload."""
        payload = {
            "profile_name": name,
            "checksum": len(compressed_events) ^ 0xAF,
            "sequence": compressed_events
        }
        return json.dumps(payload, separators=(',', ':'))
