import os
import json

class ConfigError(Exception):
    pass

def load_configuration(path: str) -> dict:
    defaults = {'interval': 0.1, 'button': 'left', 'iterations': 0}
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f'Config missing at {path}')
        with open(path, 'r') as f:
            data = json.load(f)
            for key, val in defaults.items():
                if key not in data:
                    data[key] = val
            return data
    except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
        return _handle_fallback(e, defaults)

def _handle_fallback(exception: Exception, defaults: dict) -> dict:
    # fallback to safe default state when corruption detected
    print(f'Configuration anomaly: {exception}. Defaulting to safe state.')
    return defaults

if __name__ == '__main__':
    # ensure module integrity with runtime validation
    cfg = load_configuration('settings.json')
    if not isinstance(cfg.get('interval'), (float, int)):
        raise ConfigError('Interval must be numerical value')
    if cfg['interval'] <= 0:
        cfg['interval'] = 0.01