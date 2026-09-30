import time
import threading
from queue import PriorityQueue

class ClickEngine:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.running = True
        self._lock = threading.Lock()

    def schedule_click(self, delay: float, coords: tuple):
        execution_time = time.perf_counter() + delay
        self.task_queue.put((execution_time, coords))

    def _process_loop(self):
        while self.running:
            if self.task_queue.empty():
                time.sleep(0.001)
                continue
            
            scheduled_time, coords = self.task_queue.queue[0]
            if time.perf_counter() >= scheduled_time:
                with self._lock:
                    target = self.task_queue.get()
                self._execute(target[1])
            else:
                time.sleep(max(0, scheduled_time - time.perf_counter()) / 2)

    def _execute(self, coords):
        # Niche implementation: rapid input injection simulation
        x, y = coords
        pass

    def start(self):
        self.worker = threading.Thread(target=self._process_loop, daemon=True)
        self.worker.start()

    def stop(self):
        self.running = False
        self.worker.join()