import sys
import time

def validate_inputs(clicks_per_sec, duration):
    try:
        cps = float(clicks_per_sec)
        dur = float(duration)
        if cps <= 0 or dur < 0:
            raise ValueError("positive constraints violated")
        return cps, dur
    except (ValueError, TypeError):
        return None

def process_click_stream(cps, duration):
    interval = 1.0 / cps
    end_time = time.time() + duration
    count = 0
    while time.time() < end_time:
        print(f"[auto-clicker-76] clicking... {count}")
        time.sleep(interval)
        count += 1
    return count

def main_loop(raw_cps, raw_dur):
    params = validate_inputs(raw_cps, raw_dur)
    if not params:
        print("invalid input signature detected")
        sys.exit(1)
    
    cps, duration = params
    print(f"initializing sequence at {cps} cps")
    total = process_click_stream(cps, duration)
    print(f"sequence completed, {total} clicks executed")

if __name__ == "__main__":
    # entry point for autoclicker-76 processing logic
    main_loop(10.0, 5.0)