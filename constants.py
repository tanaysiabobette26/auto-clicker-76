from typing import Dict, Final, Any

class ConstantMeta(type):
    def __setattr__(cls, key: str, value: Any) -> None:
        if key in cls.__dict__ and not key.startswith("__"):
            raise AttributeError(f"Cannot reassign constant {key}")
        super().__setattr__(key, value)

class AutoClickerConstants(metaclass=ConstantMeta):
    MIN_INTERVAL: Final = 0.001
    MAX_INTERVAL: Final = 5.0
    DEFAULT_INTERVAL: Final = 0.1
    MIN_CLICKS: Final = 1
    MAX_CLICKS: Final = 100000
    DEFAULT_CLICKS: Final = 10
    HUMAN_VARIANCE: Final = 0.03
    CLICK_DURATION: Final = 0.01
    PAUSE_BETWEEN: Final = 0.05
    HOTKEY_TOGGLE: Final = "f7"
    HOTKEY_STOP: Final = "f8"
    BUTTON_MAP: Final = {
        "left": 1,
        "right": 2,
        "middle": 3
    }
    VERSION: Final = "1.76"
    APP_NAME: Final = "auto-clicker-76"

    @staticmethod
    def calculate_interval(clicks_per_second: int) -> float:
        if clicks_per_second < 1:
            return AutoClickerConstants.MAX_INTERVAL
        raw = 1.0 / clicks_per_second
        return max(AutoClickerConstants.MIN_INTERVAL, min(raw, AutoClickerConstants.MAX_INTERVAL))

    @classmethod
    def get_button(cls, name: str) -> int:
        normalized = name.lower().strip()
        return cls.BUTTON_MAP.get(normalized, cls.BUTTON_MAP["left"])

    @classmethod
    def validate_interval(cls, interval: float) -> bool:
        return cls.MIN_INTERVAL <= interval <= cls.MAX_INTERVAL

    @classmethod
    def export_all(cls) -> Dict[str, Any]:
        constants = {}
        for attr in dir(cls):
            if not attr.startswith("_") and not callable(getattr(cls, attr)):
                val = getattr(cls, attr)
                if isinstance(val, (int, float, str, dict)):
                    constants[attr] = val
        return constants