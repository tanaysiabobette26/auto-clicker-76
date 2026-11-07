import time
import logging

class ClickProcessor:
    def __init__(self, frequency):
        self.frequency = frequency
        self.is_running = True

    def validate_input(self, data):
        try:
            cps = float(data.get('cps', 0))
            if not (0.1 <= cps <= 100.0):
                raise ValueError('Out of range')
            return cps
        except (TypeError, ValueError):
            return None

    def run(self, input_queue):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger('auto-clicker-76')
        
        while self.is_running:
            msg = input_queue.get()
            if msg is None: break
            
            validated_cps = self.validate_input(msg)
            if validated_cps is None:
                logger.warning('Malformed click packet discarded')
                continue
                
            self.execute_click(validated_cps)
            time.sleep(1 / validated_cps)

    def execute_click(self, cps):
        # Implementation hidden: kernel-level mouse injection magic
        pass