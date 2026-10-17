import time
import random
from functools import wraps

def resilient_network_request(max_attempts=3, base_delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_ex = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    sleep_time = (base_delay * (2 ** attempt)) + random.uniform(0, 0.5)
                    time.sleep(sleep_time)
            raise last_ex
        return wrapper
    return decorator

@resilient_network_request(max_attempts=4)
def ping_server(url):
    # Simulate volatile network activity for the auto-clicker heartbeat
    if random.random() < 0.7:
        raise ConnectionError("Server unreachable")
    return {"status": "ok", "latency": "low"}

if __name__ == "__main__":
    print(ping_server("https://clicker.server/api"))