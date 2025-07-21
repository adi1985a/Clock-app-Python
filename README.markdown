# ⏰🖥️ PyTimeKeep GUI: Python Clock, Alarm & Timer App ⏳
A modern, graphical Python application for real-time clock display, alarms, and countdown timers. Built with Tkinter for a beautiful, cross-platform user experience.

License: MIT | Python Platform

---

📋 **Table of Contents**
- [Overview](#overview)
- [Key Features](#key-features)
- [Screenshots](#screenshots)
- [System Requirements](#system-requirements)
- [Installation and Setup](#installation-and-setup)
- [Usage Guide](#usage-guide)
- [File Structure](#file-structure)
- [Technical Notes](#technical-notes)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📄 Overview
**PyTimeKeep GUI** is a versatile, user-friendly Python desktop app by Adrian Lesniak. It provides a live digital clock, settable alarms, and countdown timers—all in a colorful, intuitive graphical interface. The app saves your alarm/timer history, logs errors, and is fully cross-platform (Windows, macOS, Linux).

<br> 
<p align="center">
  <img src="screenshots/1.gif" width="90%">
</p>
<br>

---

## ✨ Key Features

🖥️ **Modern GUI (Tkinter):**
- Beautiful, responsive, and colorful interface
- All features accessible via buttons—no command line needed

🕒 **Live Clock:**
- Large, real-time digital clock display
- Always visible in the main window

🔔 **Alarm:**
- Set alarms for any hour and minute
- See a live countdown until the alarm triggers
- Alarm notification shown in the main window

⏳ **Countdown Timer:**
- Set a timer in MM:SS format
- Live countdown in the main window
- Notification when the timer ends

📜 **History:**
- View the last 10 alarms and timers
- Data saved in `history.json` for persistence

🛡️ **Error Logging:**
- All errors are logged to `app.log` for troubleshooting

🌈 **Fully in English**

👤 **Author and Menu Info Always Visible**

---

## 🖼️ Screenshots

<p align="center">
  <img src="screenshots\1.jpg" width="300"/>
  <img src="screenshots\2.jpg" width="300"/>
  <img src="screenshots\3.jpg" width="300"/>
  <img src="screenshots\4.jpg" width="300"/>
  <img src="screenshots\5.jpg" width="300"/>
</p>


---

## ⚙️ System Requirements
- **Python Version:** 3.7 or higher
- **Libraries:** Tkinter (included with most Python installations)
- **OS:** Windows, macOS, or Linux
- **No external dependencies required**

---

## 🛠️ Installation and Setup
1. **Clone or download the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Ensure Python 3.7+ is installed:**
   ```bash
   python --version
   # or
   python3 --version
   ```
3. **Run the application:**
   ```bash
   python main.py
   # or
   python3 main.py
   ```

---

## 💡 Usage Guide

### 📋 Main Menu (GUI)
- **Show current time:** Displays a large, live-updating clock.
- **Set alarm:** Enter hour and minute, see countdown and notification in the main window.
- **Set timer:** Enter time in MM:SS, see countdown and notification in the main window.
- **History:** View the last 10 alarms and timers set.
- **Exit:** Close the application.

All actions are performed in the main window—no popups or command line required.

---

## 🗂️ File Structure
```
├── main.py           # Main Python script with all GUI logic
├── README.markdown   # Project documentation
├── history.json      # Saved alarm/timer history (auto-created)
├── app.log           # Error log file (auto-created)
```

---

## 📝 Technical Notes
- **Alarm Scheduling:** Alarms are always set for the next occurrence (if the time has passed today, it will trigger tomorrow).
- **Timer Format:** Must be MM:SS. Invalid input is handled gracefully.
- **Threading:** Used for non-blocking countdowns and alarms.
- **Data Persistence:** History is saved to `history.json`.
- **Error Logging:** All exceptions are logged to `app.log`.
- **No command-line arguments:** All features are available via the GUI.

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork and clone the repository
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Make your changes to `main.py`
4. Commit: `git commit -m "Feature: Add your feature"`
5. Push: `git push origin feature/YourFeature`
6. Open a Pull Request

**Please ensure:**
- Code is clean, readable, and PEP8-compliant
- Use type hints where appropriate
- Comment your code where necessary

---

## 📃 License
This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact
Application by Adrian Lesniak.
For questions or suggestions, open an issue on GitHub or contact the repository maintainer.

---

🔧 Your reliable Python companion for managing time, alarms, and countdowns—with a beautiful GUI!