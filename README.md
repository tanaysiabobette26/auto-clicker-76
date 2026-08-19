# auto-clicker-76

auto-clicker-76 is a simple yet powerful Python-based autoclicker designed to automate mouse clicks with customizable settings, ideal for users looking to enhance productivity in repetitive tasks. With intuitive controls and lightweight operation, this tool allows seamless integration into daily workflows.

## Features
- **Customizable Click Intervals**: Adjust the frequency of clicks in milliseconds to suit your specific needs.
- **Hotkey Activation**: Start and stop the autoclicker using easy-to-configure keyboard shortcuts for quick accessibility.
- **Multi-Platform Compatibility**: Developed to work on Windows, macOS, and Linux, ensuring versatility for all users.
- **User-Friendly Interface**: Simple command-line interface that requires minimal setup, making it accessible for users of all experience levels.

## Installation

To install auto-clicker-76, you'll need Python 3.6 or higher. Use the following commands to clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/auto-clicker-76.git
cd auto-clicker-76
pip install -r requirements.txt
```

## Basic Usage

After installation, you can launch the autoclicker by running the following command in your terminal:

```bash
python autoclicker.py
```

You can set the click interval and define the activation hotkeys in the configuration settings. Here's a quick example of how to start the autoclicker clicking every 100 milliseconds with the F9 key:

```python
import autoclicker

# Customize your settings
autoclicker.set_click_interval(100)  # in milliseconds
autoclicker.set_hotkey('F9')          # toggle start/stop

autoclicker.start()                    # start the autoclicker
```

## License

This project is licensed under the MIT License. ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

For more details, please refer to the [LICENSE](LICENSE) file in this repository. 

---
By automating tedious clicking tasks, auto-clicker-76 frees your hands for more important activities, enhancing productivity and efficiency in your daily routines.