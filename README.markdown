# ⏰🔔 PyTimeKeep: Python CLI Clock, Alarm & Timer ⏳
_A Python command-line application providing real-time clock display, settable alarms, and countdown timers, utilizing threading for concurrent operations and supporting command-line arguments._

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
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
**Setting a Timer via CLI:**
Setting a Timer via CLI:
python clock.py -timer 00:05
Use code with caution.
Bash
Conceptual output from timer:
Timer started for 00:05.
Time remaining: 00:04
Time remaining: 00:03
...
TIMER FINISHED!
Use code with caution.
Text
⚙️ System Requirements
Python Version: Python 3.6 or higher.
Standard Python Libraries:
time
datetime
argparse (for command-line argument parsing)
threading (for concurrent operations)
sched (for scheduling alarm events)
(No external third-party libraries are required).
Operating System: Any OS that supports Python 3.6+ (e.g., Windows, macOS, Linux).
🛠️ Installation and Setup
Clone or Download the Repository:
git clone <repository-url>
cd <repository-directory>
Use code with caution.
Bash
(Replace <repository-url> and <repository-directory> if applicable, or simply download/save clock.py).
Ensure Python is Installed:
Verify you have Python 3.6 or newer installed and available in your system's PATH. You can check with python --version or python3 --version.
No Additional Library Installation Required:
The application relies solely on Python's standard libraries.
Run the Application:
Open a terminal or command prompt, navigate to the directory where you saved clock.py, and execute:
python clock.py
Use code with caution.
Bash
or if you use python3 alias:
python3 clock.py
Use code with caution.
Bash
💡 Usage Guide (Menu & Command-Line)
Interactive Menu Mode:
Launch the application without any command-line arguments:
python clock.py
Use code with caution.
Bash
The main menu will be displayed:
Show Current Time
Set Alarm
Exit
Enter the number corresponding to your choice:
Option 1 (Show Current Time): Displays the current time, updating every second. Press Enter to stop the time display and return to the main menu.
Option 2 (Set Alarm):
Prompts you to enter the desired alarm hour (0-23).
Prompts you to enter the desired alarm minute (0-59).
A countdown to the alarm will be shown. When the alarm triggers, a message (and/or beep) will occur. Press Enter to acknowledge and return to the menu.
Option 3 (Exit): Closes the application.
Command-Line Argument Mode:
To set an alarm directly:
python clock.py -alarm
Use code with caution.
Bash
This will immediately take you to the alarm setting prompts (hour and minute).
To set a timer directly:
python clock.py -timer MM:SS
Use code with caution.
Bash
Replace MM:SS with the desired duration. For example, for 1 minute and 30 seconds:
python clock.py -timer 01:30
Use code with caution.
Bash
The timer will start, display the countdown, and notify upon completion.
After command-line initiated tasks (like alarm setup or timer completion), the behavior for returning to a menu or exiting might differ based on implementation (e.g., it might exit directly or prompt to press Enter).
🗂️ File Structure
clock.py: The single Python script containing all application logic, including functions/classes for time display, alarm setting, timer management, menu handling, and command-line argument parsing.
README.md: This documentation file.
(No external data files or log files are mentioned as being created by this application in the provided description.)
📝 Technical Notes
Alarm Scheduling: The alarm uses Python's sched module to schedule an event (the alarm trigger) at a future time. It correctly calculates the next occurrence if the specified alarm time has already passed for the current day.
Timer Input Format: The timer input via command-line (-timer MM:SS) must adhere strictly to the MM:SS format. The description notes "invalid inputs may cause errors," suggesting that robust parsing and validation for this format within the script are important.
Threading for Non-Blocking UI: The use of threading allows the current time to update continuously or an alarm countdown to proceed without freezing the main part of the application, enabling the user to, for example, press Enter to return to the menu while these are active.
Lightweight and Portable: Requiring no external dependencies beyond standard Python makes the application easy to run on any system with a compatible Python interpreter.
Potential Enhancements:
Adding sound alerts for alarms and timers (e.g., using winsound on Windows, or a cross-platform library like playsound).
More robust input validation, especially for the timer format.
Persistent alarms (saving/loading alarm settings to/from a file).
A more sophisticated visual display in the console (e.g., using libraries like curses on Unix-like systems, or more advanced character art).
🤝 Contributing
Contributions to PyTimeKeep are highly encouraged! If you have ideas for:
Adding sound alerts for alarms/timers in a cross-platform way.
Implementing persistent storage for alarms.
Improving the console UI/UX.
Adding more time-related features (e.g., stopwatch, world clock).
Refactoring for better code organization if the script grows complex.
Fork the repository.
Create a new branch for your feature (git checkout -b feature/SoundAlerts).
Make your changes to clock.py.
Commit your changes (git commit -m 'Feature: Add cross-platform sound alerts').
Push to the branch (git push origin feature/SoundAlerts).
Open a Pull Request.
Please ensure your code is well-commented and follows Python best practices (e.g., PEP 8), including type hints where appropriate.
📃 License
This project is licensed under the MIT License.
(If you have a LICENSE file in your repository, refer to it: See the LICENSE file for details.)
📧 Contact
Application concept by Adrian Lesniak.
For questions or feedback, please open an issue on the GitHub repository or contact the repository owner.
🔧 Your reliable Python companion for managing time, alarms, and countdowns from the command line!
