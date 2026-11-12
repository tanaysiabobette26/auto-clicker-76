import json
from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Optional
from pathlib import Path

@dataclass
class ClickerConfig:
    cps: float = 10.0
    button: str = "left"
    jitter_px: int = 2
    hotkey: str = "f8"
    randomize_interval: bool = True
    presets: Dict[str, Dict[str, Any]] = field(default_factory=lambda: {
        "fast": {"cps": 50.0, "jitter_px": 0},
        "stealth": {"cps": 7.5, "jitter_px": 5},
    })

    def sanitize(self) -> None:
        """Enforce strict boundaries on config parameters."""
        self.cps = max(0.1, min(self.cps, 500.0))
        self.jitter_px = max(0, min(self.jitter_px, 100))
        valid_buttons = ("left", "right", "middle")
        self.button = self.button.lower() if self.button.lower() in valid_buttons else "left"

    def apply_preset(self, name: str) -> bool:
        if name not in self.presets:
            return False
        for key, value in self.presets[name].items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.sanitize()
        return True

    def export_json(self, filepath: Path) -> None:
        self.sanitize()
        filepath.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")

    @classmethod
    def load_or_default(cls, filepath: Path) -> "ClickerConfig":
        if filepath.exists():
            try:
                data = json.loads(filepath.read_text(encoding="utf-8"))
                valid_keys = cls.__annotations__.keys()
                cfg = cls(**{k: v for k, v in data.items() if k in valid_keys})
                cfg.sanitize()
                return cfg
            except (json.JSONDecodeError, TypeError):
                pass
        return cls()

class ConfigRegistry:
    """Dynamic wrapper for runtime config state cleanup."""
    _instance: Optional[ClickerConfig] = None

    @classmethod
    def get(cls) -> ClickerConfig:
        if cls._instance is None:
            cls._instance = ClickerConfig()
        return cls._instance

    @classmethod
    def reset(cls) -> None:
        cls._instance = ClickerConfig()
