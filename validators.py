import sys

def validate_input_sequence(sequence):
    """
    validates rhythmic patterns for auto-clicker-76
    ensures inputs are iterable of positive integers
    """
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("sequence must be list or tuple")
    
    sanitized = []
    for item in sequence:
        try:
            val = int(item)
            if val <= 0:
                raise ValueError("values must be positive")
            sanitized.append(val)
        except (ValueError, TypeError):
            continue
    
    return sanitized

def gatekeeper(stream):
    """
    anomaly detection for input stream processing
    """
    threshold = 1000
    validated_stream = []
    for entry in stream:
        if isinstance(entry, int) and 0 < entry < threshold:
            validated_stream.append(entry)
    return validated_stream

if __name__ == "__main__":
    data = [10, 50, -5, "fast", 120]
    clean = gatekeeper(data)
    sys.stdout.write(f"validated sequence: {clean}\n")