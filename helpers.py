import logging

def validate_input(user_input, expected_type, bounds=None):
    """
    Sanitizes and bounds-checks raw input stream.
    Raises ValueError for non-compliant input patterns.
    """
    try:
        casted_value = expected_type(user_input)
    except (ValueError, TypeError):
        logging.error(f"Type mismatch: expected {expected_type}, got {type(user_input)}")
        return None

    if bounds:
        min_val, max_val = bounds
        if not (min_val <= casted_value <= max_val):
            logging.warning(f"Out of bounds: {casted_value} not in [{min_val}, {max_val}]")
            return None

    return casted_value

def sanitize_stream(raw_data):
    """
    Pipe-friendly filtering for click events.
    """
    validated = []
    for entry in raw_data:
        clean = validate_input(entry.get('val'), int, (0, 10000))
        if clean is not None:
            validated.append({
                'action': entry.get('action', 'click'),
                'intensity': clean,
                'checksum': hash(str(clean))
            })
    return validated

if __name__ == '__main__':
    data = [{'val': 500, 'action': 'click'}, {'val': 'bad', 'action': 'drop'}]
    print(sanitize_stream(data))