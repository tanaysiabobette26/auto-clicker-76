import logging
import logging.handlers
from pathlib import Path
import sys


class BurstLogFormatter(logging.Formatter):
    """Custom formatter injecting click burst badges and CPS indicators."""

    BADGES = {
        logging.DEBUG: "[TRACE]",
        logging.INFO: "[CLICK]",
        logging.WARNING: "[BURST]",
        logging.ERROR: "[ERROR]",
        logging.CRITICAL: "[HALT]",
    }

    def format(self, record: logging.LogRecord) -> str:
        badge = self.BADGES.get(record.levelno, "[LOG]")
        cps = getattr(record, "cps", None)
        record.click_badge = f"{badge} @ {cps:.1f} CPS" if cps is not None else badge
        return super().format(record)


def configure_autoclick_logger(
    name: str = "auto_clicker",
    log_dir: str = "logs",
    max_mb: float = 1.0,
    backups: int = 5,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    folder = Path(log_dir)
    folder.mkdir(parents=True, exist_ok=True)

    log_format = "%(asctime)s | %(click_badge)s | %(message)s"
    formatter = BurstLogFormatter(fmt=log_format, datefmt="%H:%M:%S")

    file_handler = logging.handlers.RotatingFileHandler(
        filename=folder / f"{name}.log",
        maxBytes=int(max_mb * 1024 * 1024),
        backupCount=backups,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    app_log = configure_autoclick_logger()
    app_log.info("Engine armed", extra={"cps": 0.0})
    app_log.warning("High speed burst initiated", extra={"cps": 60.5})
