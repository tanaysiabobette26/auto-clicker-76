import json
import base64
import zlib
from typing import Dict, Any

class ClickProfileProcessor:
    def __init__(self, secret_key: bytes = b'click-key-76'):
        self.key = secret_key

    def encode_config(self, data: Dict[str, Any]) -> str:
        raw_data = json.dumps(data).encode()
        compressed = zlib.compress(raw_data)
        obfuscated = bytearray(b ^ self.key[i % len(self.key)] for i, b in enumerate(compressed))
        return base64.urlsafe_b64encode(obfuscated).decode()

    def decode_config(self, token: str) -> Dict[str, Any]:
        raw_bytes = base64.urlsafe_b64decode(token)
        deobfuscated = bytes(b ^ self.key[i % len(self.key)] for i, b in enumerate(raw_bytes))
        decompressed = zlib.decompress(deobfuscated)
        return json.loads(decompressed.decode())

    @staticmethod
    def sanitize_intervals(data: Dict[str, Any]) -> Dict[str, Any]:
        """Forces millisecond bounds for safety."""
        if 'interval' in data:
            data['interval'] = max(1, min(data['interval'], 60000))
        return data

if __name__ == '__main__':
    proc = ClickProfileProcessor()
    payload = {'interval': 50, 'button': 'left', 'repeat': True}
    encoded = proc.encode_config(payload)
    print(f'Encoded payload: {encoded}')
    print(f'Decoded payload: {proc.decode_config(encoded)}')