# auto-clicker-76

`auto-clicker-76` is a high-performance, lightweight Python automation tool designed to handle repetitive clicking tasks with precision. It offers a clean, non-intrusive interface for users who require reliable background execution without unnecessary system overhead.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Features

*   **Configurable Intervals:** Set precise delays between clicks in milliseconds or seconds to mimic human-like or machine-speed input.
*   **Dynamic Hotkey Control:** Start and stop the clicking sequence instantly using globally registered hotkeys, even when the application is minimized.
*   **Coordinate Precision:** Target specific areas on your monitor with pixel-perfect coordinate locking.
*   **Low CPU Footprint:** Built with native threading, ensuring zero lag for your primary applications while the script runs in the background.

### Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed. Clone this repository and install the required dependencies:

```bash
git clone https://github.com/Developer/auto-clicker-76.git
cd auto-clicker-76
pip install -r requirements.txt
```

### Usage

To start the auto-clicker with the default settings (100ms interval, left-click), execute:

```bash
python main.py --interval 0.1 --button left
```

**Configuration Options:**
*   `--interval`: Time delay between clicks in seconds (e.g., `0.5`).
*   `--button`: Specify `left`, `right`, or `middle` mouse button.
*   `--toggle`: Set the key to trigger the start/stop state (default: `F6`).

### Safety Note
This tool is intended for personal productivity and software testing automation. Please respect the Terms of Service of any third-party applications or websites where you intend to use this software. 

### License
This project is licensed under the [MIT License](LICENSE).