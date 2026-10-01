import json
import base64
import zlib
from typing import Any, Dict

class ClickProfileProcessor:
    """Binary-packed serialization for high-frequency click patterns."""
    
    def __init__(self, secret_key: int = 0x76):
        self.key = secret_key

    def pack(self, data: Dict[str, Any]) -> str:
        raw_json = json.dumps(data).encode('utf-8')
        compressed = zlib.compress(raw_json, level=9)
        obfuscated = bytes([b ^ self.key for b in compressed])
        return base64.b85encode(obfuscated).decode('ascii')

    def unpack(self, payload: str) -> Dict[str, Any]:
        obfuscated = base64.b85decode(payload)
        compressed = bytes([b ^ self.key for b in obfuscated])
        decompressed = zlib.decompress(compressed)
        return json.loads(decompressed.decode('utf-8'))

    @staticmethod
    def sanitize_intervals(intervals: list) -> list:
        """Enforce sanity bounds on click timings."""
        return [max(1, min(int(x), 60000)) for x in intervals]

# Singleton instance for global app usage
processor = ClickProfileProcessor()