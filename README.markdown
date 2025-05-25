# ⏰🔔 PyTimeKeep: Python CLI Clock, Alarm & Timer ⏳
_A Python command-line application providing real-time clock display, settable alarms, and countdown timers, utilizing threading for concurrent operations and supporting command-line arguments._

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://www.python.org/downloads/)

---
<!-- No specific external libraries to badge beyond standard Python modules -->

## 📋 Table of Contents
1.  [Overview](#-overview)
2.  [Key Features](#-key-features)
3.  [Screenshots (Conceptual CLI Output)](#-screenshots-conceptual-cli-output)
4.  [System Requirements](#-system-requirements)
5.  [Installation and Setup](#️-installation-and-setup)
6.  [Usage Guide (Menu & Command-Line)](#️-usage-guide-menu--command-line)
7.  [File Structure](#-file-structure)
8.  [Technical Notes](#-technical-notes)
9.  [Contributing](#-contributing)
10. [License](#-license)
11. [Contact](#-contact)

## 📄 Overview

**PyTimeKeep** is a versatile Python command-line tool designed to offer essential time-keeping functionalities. Developed by Adrian Lesniak, it provides a real-time display of the current time, allows users to set alarms for specific hours and minutes using Python's `sched` module, and can run countdown timers based on user-defined durations. The application leverages Python's `threading` module to ensure non-blocking updates for the time display and alarm countdowns. Users can interact with PyTimeKeep through a simple menu or by using command-line arguments for direct access to alarm or timer functions.

## ✨ Key Features

*   🕒 **Real-Time Clock Display**:
    *   Shows the current system time, updating every second in the console.
    *   Operates in a separate thread to allow continued interaction or other functions.
*   🔔 **Alarm Functionality**:
    *   Set alarms for a specific hour (0-23) and minute (0-59).
    *   Displays a countdown to the set alarm time.
    *   The alarm is scheduled for its next occurrence (e.g., if the specified time has already passed today, it will be set for the next day).
    *   (Assumed: Triggers a console message or a simple beep when the alarm time is reached).
*   ⏳ **Countdown Timer**:
    *   Run a countdown timer based on a user-specified duration in MM:SS (minutes:seconds) format.
    *   Displays the remaining time, updating every second.
    *   (Assumed: Triggers a console message or beep upon completion).
*   ⌨️ **Command-Line Argument Support**:
    *   Launch directly into alarm setting mode: `python clock.py -alarm`
    *   Launch directly into timer mode with a specified duration: `python clock.py -timer MM:SS` (e.g., `01:30` for 1 minute 30 seconds).
*   🧵 **Threading for Concurrency**:
    *   Utilizes Python's `threading` module to manage the continuous time display and alarm countdowns in the background without blocking the main user interface or menu interaction.
*   📋 **Interactive Menu**:
    *   Provides a simple numbered menu for users to choose between showing the current time, setting an alarm, or exiting the application.

## 🖼️ Screenshots (Conceptual CLI Output)

**Conceptual Output Examples:**

**Main Menu:**
```text
--- PyTimeKeep: CLI Clock, Alarm & Timer ---
1. Show Current Time
2. Set Alarm
3. Exit
Enter your choice:
```
**Current Time Display:**
```text
Current Time: 14:35:12
Current Time: 14:35:13
Current Time: 14:35:14
(Press Enter to return to menu)
```
**Setting an Alarm:**
```text
Enter alarm hour (0-23): 15
Enter alarm minute (0-59): 00
Alarm set for 15:00:00.
Time until alarm: 00:24:45
Time until alarm: 00:24:44
...
ALARM! ALARM! ALARM!
(Press Enter to return to menu)
```

## ▶️ Setting a Timer via CLI

```bash
python clock.py -timer 00:05
```

Conceptual output from timer:

```text
Timer started for 00:05.
Time remaining: 00:04
Time remaining: 00:03
...
TIMER FINISHED!
```

---

## ⚙️ System Requirements

- **Python Version**: Python 3.6 or higher.
- **Standard Python Libraries**:
  - `time`
  - `datetime`
  - `argparse` (for command-line argument parsing)
  - `threading` (for concurrent operations)
  - `sched` (for scheduling alarm events)
- **Operating System**: Any OS that supports Python 3.6+ (Windows, macOS, Linux).
- **No external dependencies required.**

---

## 🛠️ Installation and Setup

Clone or download the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

Ensure Python 3.6+ is installed:

```bash
python --version
# or
python3 --version
```

Run the application:

```bash
python clock.py
# or
python3 clock.py
```

---

## 💡 Usage Guide (Menu & Command-Line)

### 📋 Interactive Menu Mode

Launch without arguments:

```bash
python clock.py
```

You will see:

```
1. Show Current Time
2. Set Alarm
3. Exit
```

- **Option 1 (Show Current Time)**: Displays current time (updates every second). Press Enter to stop.
- **Option 2 (Set Alarm)**: Enter hour/minute. Countdown begins. Alarm triggers at set time.
- **Option 3 (Exit)**: Exits application.

---

### ⌨️ Command-Line Argument Mode

Set an alarm directly:

```bash
python clock.py -alarm
```

Set a timer directly:

```bash
python clock.py -timer MM:SS
```

Example for 1 minute 30 seconds:

```bash
python clock.py -timer 01:30
```

The timer will countdown and notify on completion.

---

## 🗂️ File Structure

```bash
├── clock.py       # Main Python script with all features
├── README.md      # Project documentation
```

No external data or log files are used.

---

## 📝 Technical Notes

- **Alarm Scheduling**: Uses `sched` to trigger alarms at specified future times, even if the time has passed (moves to next occurrence).
- **Timer Format**: Must be in MM:SS format. Invalid input may crash.
- **Threading**: Enables non-blocking updates during alarms/timers.
- **Portable**: Requires only standard Python libraries.

---

### 🔧 Potential Enhancements

- Add cross-platform sound alerts (`winsound`, `playsound`)
- Validate timer input format robustly
- Add persistent alarms (saved to a file)
- Enhance UI (e.g., with `curses` or ASCII art)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

```bash
# Fork and clone the repository
git checkout -b feature/YourFeature
# Make changes to clock.py
git commit -m "Feature: Add your feature"
git push origin feature/YourFeature
```

Open a Pull Request. Please ensure:

- Code is clean, readable, and PEP8-compliant
- Use type hints where appropriate
- Comment your code where necessary

---

## 📃 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

Application concept by **Adrian Lesniak**.  
For questions or suggestions, open an issue on GitHub or contact the repository maintainer.

---

> 🔧 Your reliable Python companion for managing time, alarms, and countdowns from the command line!
