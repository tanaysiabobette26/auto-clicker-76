import logging
import json
from datetime import datetime
from pathlib import Path

class ClickLogger:
    def __init__(self, log_dir: str = "logs"):
        self.log_path = Path(log_dir)
        self.log_path.mkdir(exist_ok=True)
        self.logger = logging.getLogger("auto-clicker-76")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.log_path / "session.log")
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(handler)

    def log_event(self, action: str, data: dict):
        payload = {
            "timestamp": datetime.now().isoformat(),
            "event": action,
            "details": data
        }
        self.logger.info(json.dumps(payload))

    def rotate_logs(self):
        """Compresses current logs into a datestamped archive."""
        import zipfile
        archive_name = self.log_path / f"archive_{datetime.now().strftime('%Y%m%d')}.zip"
        with zipfile.ZipFile(archive_name, 'w') as zipf:
            for log_file in self.log_path.glob("*.log"):
                zipf.write(log_file, log_file.name)
                log_file.unlink()