[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# auto-clicker-76

auto-clicker-76 is a lightweight, low-latency Python automation tool designed for high-frequency mouse clicks and background task execution. Built with configurable hotkeys and randomized interval dithering, it ensures precise click automation without triggering basic anti-bot heuristics.

## Features

* **Precision Interval Control:** Configure click rates from 1 to 1000 CPS with microsecond accuracy and optional Gaussian jitter.
* **Global Hotkey Management:** Bind custom toggle and exit keys using native system hooks that operate globally across all active windows.
* **Dual-Targeting Modes:** Seamlessly switch between fixed screen coordinate targeting and active cursor tracking.
* **Multi-Button Support:** Full execution support for left, right, and middle mouse buttons, including double-click and hold actions.

## Installation

Clone the repository and install the required system dependencies:

```bash
git clone https://github.com/Developer/auto-clicker-76.git
cd auto-clicker-76
pip install -r requirements.txt
```

## Usage

Launch the application via the CLI with custom parameters:

```bash
python main.py --cps 50 --button left --jitter 0.002
```

Or import the `ClickEngine` directly into your Python scripts:

```python
from auto_clicker import ClickEngine

# Initialize clicker at 20 CPS with standard F8 toggle key
engine = ClickEngine(
    cps=20,
    button='left',
    toggle_key='f8',
    jitter=True
)

# Start listening for global hotkeys
engine.listen()
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.