import json
from collections import deque
import time
from typing import List, Tuple, Dict, Any

class ClickDataHandler:
    def __init__(self, max_history: int = 100):
        self.history = deque(maxlen=max_history)
        self.current_sequence = []

    def add_click(self, x: int, y: int, delay: float) -> None:
        click = {"x": x, "y": y, "delay": delay, "timestamp": time.time()}
        self.history.append(click)
        self.current_sequence.append((x, y, delay))

    def get_processed_data(self) -> List[Tuple[int, int, float]]:
        if not self.current_sequence:
            return []

        delays = [d for _, _, d in self.current_sequence]
        mean_delay = sum(delays) / len(delays)
        variance = sum((d - mean_delay)**2 for d in delays) / len(delays)
        std = variance ** 0.5 if variance > 0 else 0

        processed = []
        for x, y, d in self.current_sequence:
            if std == 0 or abs(d - mean_delay) <= 2 * std:
                processed.append((x, y, d))

        unique = []
        prev = None
        for click in processed:
            if click != prev:
                unique.append(click)
                prev = click

        return unique

    def save_to_file(self, filename: str) -> None:
        data = list(self.history)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)
        self.history = deque(data, maxlen=self.history.maxlen)
        self.current_sequence = [(item["x"], item["y"], item["delay"]) for item in data]

def handle_autoclicker_data(raw_clicks: List[Tuple[int, int, float]]) -> Dict[str, Any]:
    handler = ClickDataHandler()
    for x, y, d in raw_clicks:
        handler.add_click(x, y, d)
    processed = handler.get_processed_data()
    total_delay = sum(d for _, _, d in processed)
    return {
        "processed_clicks": processed,
        "count": len(processed),
        "total_delay": total_delay
    }

if __name__ == "__main__":
    sample_data = [(100, 150, 0.1), (100, 150, 0.2), (200, 300, 0.5), (100, 150, 0.15)]
    result = handle_autoclicker_data(sample_data)
    print(result)