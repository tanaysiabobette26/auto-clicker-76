import time
import pyautogui
import logging

class ClickerEngine:
    def __init__(self, interval: float, safety_pixel=(0, 0)):
        self.interval = interval
        self.safety_pixel = safety_pixel
        self.active = True

    def run_click_loop(self, iterations: int):
        try:
            for i in range(iterations):
                if not self.active:
                    break
                if pyautogui.position() == self.safety_pixel:
                    raise InterruptedError('Safety trigger activated')
                
                pyautogui.click()
                time.sleep(self.interval)
        except pyautogui.FailSafeException:
            logging.critical('mouse panic exit')
        except InterruptedError as e:
            logging.warning(f'forced stop: {e}')
        except Exception as e:
            logging.error(f'unforeseen mechanical failure: {type(e).__name__}')
        finally:
            self.shutdown()

    def shutdown(self):
        self.active = False
        logging.info('autoclicker session teardown complete')

def execute_task(interval: float, count: int):
    engine = ClickerEngine(interval)
    engine.run_click_loop(count)