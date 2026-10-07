# auto-clicker-76

`auto-clicker-76` is a high-performance, Python-based automation tool designed for precision mouse clicking tasks. It provides a lightweight solution for repetitive workflows, offering low-latency execution and an intuitive configuration interface.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features
*   **Dynamic CPS Control:** Adjustable clicking speed ranging from 1 to 1000 clicks per second.
*   **Smart Hotkey Mapping:** Start and stop automation instantly using customizable global keyboard shortcuts.
*   **Anti-Detection Jitter:** Optional randomization feature to vary click timing, mimicking human interaction patterns.
*   **Cross-Platform Core:** Built using `pynput` for seamless operation on Windows, macOS, and Linux environments.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/auto-clicker-76.git
cd auto-clicker-76
pip install -r requirements.txt
```

## Usage

To launch the clicker with default settings, run the following command in your terminal:

```bash
python main.py --interval 0.01 --button left
```

### Basic Implementation
You can also integrate the core clicking logic directly into your own Python scripts:

```python
from clicker import AutoClicker

# Initialize with 50ms delay between clicks
bot = AutoClicker(interval=0.05, button='left')

# Toggle clicking
bot.start()
# ... perform actions ...
bot.stop()
```

## Configuration
All hotkeys and randomized jitter settings can be adjusted in the `config.json` file located in the root directory. Modify these parameters to suit your specific desktop automation requirements.

## License
Distributed under the MIT License. See `LICENSE` for more information.