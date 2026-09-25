import time

def validate_input(val, bounds=(1, 1000)):
    try:
        num = float(val)
        return bounds[0] <= num <= bounds[1]
    except (ValueError, TypeError):
        return False

def process_clicks(cps, duration):
    if not validate_input(cps, (0.1, 100)):
        raise ValueError("invalid cps range")
    if not validate_input(duration, (1, 3600)):
        raise ValueError("invalid duration range")
    
    interval = 1.0 / float(cps)
    end_time = time.time() + float(duration)
    
    print(f"initiating sequence: {cps} clicks/sec for {duration}s")
    while time.time() < end_time:
        # simulate click logic
        time.sleep(interval)
    print("sequence complete")

if __name__ == '__main__':
    try:
        # simulating user inputs from CLI
        user_cps = "10"
        user_dur = "5"
        process_clicks(user_cps, user_dur)
    except Exception as e:
        print(f"execution error: {e}")