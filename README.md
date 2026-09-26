[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# auto-clicker-76

`auto-clicker-76` is a lightweight, high-performance Python automation tool designed for precise microsecond mouse clicking and custom hotkey triggering. It bypasses basic pattern detection using randomized click intervals while maintaining minimal CPU overhead during extended background sessions.

## Features

- **Microsecond Precision:** Configurable click rates ranging from 1 click per hour up to 1,000 clicks per second using non-blocking thread scheduling.
- **Humanized Randomization:** Built-in Gaussian noise generator to simulate natural human click intervals and prevent automated bot flag triggers.
- **Global Hotkey Binding:** Instant toggle functionality using customizable hotkeys (default `F8`) that register system-wide, even when unfocused.
- **Coordinate Locking:** Option to lock clicks to a specific screen pixel or allow free-roaming clicks at the current cursor position.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/auto-clicker-76.git
cd auto-clicker-76
pip install -r requirements.txt
```

*Dependencies: `pynput >= 1.7.6`*

## Usage

Run the clicker via the command-line interface with custom parameters:

```bash
python main.py --cps 50 --button left --randomize --key f8
```

Alternatively, import the engine directly into your Python scripts:

```python
from autoclicker import ClickEngine

# Initialize clicker: 20 clicks per second, left button, with interval variance
app = ClickEngine(
    cps=20,
    button='left',
    randomize=True,
    hotkey='f8'
)

# Start listening for the global toggle hotkey
app.start()
```

## License

Distributed under the MIT License. See `LICENSE` for more information.