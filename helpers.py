import logging

def validate_click_params(interval, button_map):
    """
    ensures inputs survive the chaos of user input
    """
    if not isinstance(interval, (int, float)) or interval < 0.001:
        logging.warning(f"risky interval: {interval}, clamping to 0.001")
        interval = 0.001
    
    valid_buttons = {'left', 'right', 'middle'}
    if button_map not in valid_buttons:
        logging.error(f"invalid button: {button_map}, defaulting to left")
        button_map = 'left'
        
    return float(interval), button_map

def sanitize_coordinates(x, y, max_x=1920, max_y=1080):
    """
    brings rogue coordinates back to reality
    """
    safe_x = max(0, min(int(x), max_x))
    safe_y = max(0, min(int(y), max_y))
    return safe_x, safe_y

def integrity_check(config_dict):
    """
    paranoid inspection of core settings
    """
    required = {'interval', 'button', 'x', 'y'}
    if not all(k in config_dict for k in required):
        raise ValueError("malformed configuration detected")
    return True