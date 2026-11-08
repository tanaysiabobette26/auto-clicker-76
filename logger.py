import datetime
import sys
import os

class AutoClickLogger:
    def __init__(self, log_file='clicker.log'):
        self.log_file = log_file
        self.stream = open(self.log_file, 'a', encoding='utf-8')

    def __del__(self):
        if hasattr(self, 'stream'):
            self.stream.close()

    def log(self, level, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted = f'[{timestamp}] [{level.upper()}] {message}'
        print(formatted)
        self.stream.write(formatted + '\n')
        self.stream.flush()

    def info(self, msg):
        self.log('info', msg)

    def error(self, msg):
        self.log('error', msg)

    @staticmethod
    def quick_trace(error):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        return f'{error} at {fname}:{exc_tb.tb_lineno}'

logger = AutoClickLogger()