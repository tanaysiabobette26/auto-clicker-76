import os
import gzip
import logging
from logging.handlers import RotatingFileHandler

class GzippedRotatingFileHandler(RotatingFileHandler):
    def rotation_filename(self, default_name):
        return default_name + ".gz"

    def rotate(self, source, dest):
        with open(source, "rb") as f_in:
            with gzip.open(dest, "wb") as f_out:
                f_out.writelines(f_in)
        os.remove(source)

def setup_logger(log_file="autoclicker.log", max_bytes=1024*1024, backup_count=5):
    logger = logging.getLogger("auto_clicker")
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d]: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler = GzippedRotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
        
    return logger