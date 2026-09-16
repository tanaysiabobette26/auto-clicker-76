# auto-clicker-76

`auto-clicker-76` is a lightweight, high-performance automation tool designed to simulate mouse clicks with precision and minimal CPU overhead. It provides a robust command-line interface for users requiring rapid, repetitive input automation for testing or productivity tasks.

## Features

*   **Configurable Intervals:** Set precise click speeds ranging from millisecond-level precision to custom delay intervals.
*   **Dynamic Hotkeys:** Start and stop automation instantly using global keyboard listeners without needing to focus the terminal.
*   **Smart Target Mode:** Supports coordinate-based clicking to target specific areas of your desktop environment.
*   **Low Latency Engine:** Built on `pynput` for cross-platform compatibility and minimal system resource footprint.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/auto-clicker-76.git
cd auto-clicker-76
pip install -r requirements.txt
```

## Usage

To start the clicker with a default interval of 0.1 seconds, run the following command:

```bash
python main.py --interval 0.1
```

**Common Flags:**
* `--button left`: Set the mouse button to `left`, `right`, or `middle`.
* `--count 100`: Execute a specific number of clicks before stopping automatically.
* `--x 500 --y 500`: Force the cursor to a specific screen coordinate before clicking.

Use the configured hotkey (default: `F6`) to toggle the clicking process on and off at any time.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.