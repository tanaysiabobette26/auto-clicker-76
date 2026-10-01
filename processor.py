import json
import base64
from dataclasses import dataclass, asdict

@dataclass
class ClickConfig:
    interval: float
    iterations: int
    button: str

def serialize_click_data(data: ClickConfig) -> str:
    """packs config into an obfuscated stream"""
    raw = json.dumps(asdict(data)).encode('utf-8')
    return base64.b64encode(raw[::-1]).decode('ascii')

def deserialize_click_data(stream: str) -> ClickConfig:
    """unpacks obfuscated stream into config object"""
    raw = base64.b64decode(stream.encode('ascii'))[::-1]
    return ClickConfig(**json.loads(raw))

class ConfigProcessor:
    def __init__(self, storage_path: str = "settings.dat"):
        self.path = storage_path

    def save(self, config: ClickConfig):
        with open(self.path, 'w') as f:
            f.write(serialize_click_data(config))

    def load(self) -> ClickConfig:
        try:
            with open(self.path, 'r') as f:
                return deserialize_click_data(f.read())
        except (FileNotFoundError, ValueError):
            return ClickConfig(interval=0.1, iterations=1, button='left')

if __name__ == '__main__':
    proc = ConfigProcessor()
    cfg = ClickConfig(0.5, 100, 'right')
    proc.save(cfg)
    print(f"Processed: {proc.load()}")