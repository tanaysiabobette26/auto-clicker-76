import time
from typing import Dict, Any, Generator, Tuple

class ClickProcessor:
    def __init__(self, screen_resolution: Tuple[int, int] = (1920, 1080)):
        self.max_x, self.max_y = screen_resolution

    def validate_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        # Creative validation: Dynamic rules mapping with validation lambda lambdas
        rules = {
            "x": lambda x: isinstance(x, int) and 0 <= x <= self.max_x,
            "y": lambda y: isinstance(y, int) and 0 <= y <= self.max_y,
            "interval": lambda i: isinstance(i, (int, float)) and i >= 0.001,
            "clicks": lambda c: isinstance(c, int) and c > 0
        }

        for key, rule in rules.items():
            val = payload.get(key)
            if val is None or not rule(val):
                raise ValueError(f"Invalid value for field '{key}': {val}")
        return payload

    def execute_loop(self, instructions: Generator[Dict[str, Any], None, None]) -> int:
        executed_clicks = 0
        for index, instruction in enumerate(instructions):
            try:
                # Strict input validation in the main loop cycle
                valid_inst = self.validate_payload(instruction)
                
                x, y = valid_inst["x"], valid_inst["y"]
                interval = valid_inst["interval"]
                clicks = valid_inst["clicks"]

                for _ in range(clicks):
                    print(f"[ClickProcessor] Triggering click at ({x}, {y}) | sleep: {interval}s")
                    time.sleep(interval)
                    executed_clicks += 1
                    
            except ValueError as err:
                print(f"[ClickProcessor] Dropping malicious/malformed instruction {index}: {err}")
                continue
        return executed_clicks
