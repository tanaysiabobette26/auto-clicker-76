# auto-clicker-76

`auto-clicker-76` is a high-performance, lightweight automation tool designed to simulate mouse input with millisecond precision. Built for task automation and repetitive workflow efficiency, it provides a stable interface for managing complex clicking sequences.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

### Features

*   **Custom Interval Control:** Define precise delays between clicks (in milliseconds) to match specific application response times.
*   **Dynamic Hotkeys:** Start and stop automation instantly using global keyboard shortcuts, allowing for seamless integration while working.
*   **Variable Click Modes:** Toggle between single-click, double-click, and hold-to-drag functionalities with a unified command structure.
*   **Resource Optimized:** Utilizes low-level system hooks to ensure minimal CPU usage, even during rapid, high-frequency execution.

### Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed on your system. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/auto-clicker-76.git
cd auto-clicker-76
pip install -r requirements.txt
```

### Basic Usage

You can launch the clicker directly from your terminal. To initiate a standard click stream at 100ms intervals, use the following command:

```bash
python main.py --interval 100 --mode single
```

**Common Flags:**
*   `--interval`: Set the delay in milliseconds (default: 500).
*   `--button`: Specify the mouse button (`left`, `right`, or `middle`).
*   `--limit`: Set a specific number of clicks before auto-terminating.

Once running, press `F8` to toggle the clicking state globally, or `Esc` to exit the application entirely.

### License

Distributed under the MIT License. See `LICENSE` for more information.