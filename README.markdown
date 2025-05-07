# Clock Application

## Overview
Clock Application is a Python command-line tool that provides time display, alarm, and timer functionalities. It shows the current time in real-time, sets alarms using a scheduler, and runs countdown timers. Built with threading for concurrent updates and supports command-line arguments.

## Features
- **Time Display**: Shows the current time, updated every second.
- **Alarm**: Sets alarms for a specific hour and minute, with a countdown display.
- **Timer**: Runs a countdown timer based on user-specified minutes and seconds (MM:SS).
- **Command-Line Support**: Launch with `-alarm` to set an alarm or `-timer MM:SS` for a timer.
- **Threading**: Uses threads for non-blocking time display and alarm countdowns.

## Requirements
- Python 3.6+
- Standard libraries (no external dependencies):
  - `time`
  - `datetime`
  - `argparse`
  - `threading`
  - `sched`

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. No additional libraries are required.
3. Run the application:
   ```bash
   python clock.py
   ```

## Usage
1. Launch the app to access the main menu.
2. **Menu Options**:
   - **1. Show Current Time**: Displays the current time, updated every second. Press Enter to return to the menu.
   - **2. Set Alarm**: Enter hour (0-23) and minute (0-59) for the alarm. Shows countdown until the alarm triggers.
   - **3. Exit**: Closes the application.
3. **Command-Line Options**:
   - Set an alarm: `python clock.py -alarm`
   - Set a timer: `python clock.py -timer MM:SS` (e.g., `python clock.py -timer 01:30`)
4. Press Enter to return to the menu after time display or alarm setup.

## File Structure
- `clock.py`: Main script containing all application logic, including time display, alarm, and timer functions.
- `README.md`: This file, providing project documentation.

## Notes
- The alarm is scheduled for the next occurrence (e.g., next day if the time has passed).
- Timer input must be in `MM:SS` format; invalid inputs may cause errors.
- Threading ensures non-blocking time updates, but the app waits for Enter to return to the menu.
- No external dependencies are required, making it lightweight and portable.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, open an issue on GitHub or contact the repository owner.