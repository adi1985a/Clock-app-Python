"""
Aplikacja zegarowa z funkcją zegarka, budzika i timera.
Autor: Adrian Lesniak

Opis:
- Zegar: wyświetla aktualny czas.
- Budzik: ustawia alarm na wybraną godzinę i minutę.
- Timer: odlicza czas do zera.
- Historia alarmów i timerów zapisywana do pliku.
- Obsługa wyjątków i logowanie błędów do pliku.
- Przygotowanie pod graficzny interfejs użytkownika (GUI, tkinter).
"""

import time
import datetime
import threading
import sched
import json
import logging
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import queue

# Konfiguracja loggera
class LoggerSingleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            logging.basicConfig(filename='app.log', level=logging.ERROR,
                                format='%(asctime)s %(levelname)s: %(message)s')
        return cls._instance
    @staticmethod
    def log_error(msg):
        logging.error(msg)

# Klasa do obsługi historii
class HistoryManager:
    FILE = 'history.json'
    @staticmethod
    def load():
        if not os.path.exists(HistoryManager.FILE):
            return []
        try:
            with open(HistoryManager.FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            LoggerSingleton.log_error(f'Błąd odczytu historii: {e}')
            return []
    @staticmethod
    def save(entry):
        history = HistoryManager.load()
        history.append(entry)
        try:
            with open(HistoryManager.FILE, 'w', encoding='utf-8') as f:
                json.dump(history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            LoggerSingleton.log_error(f'Błąd zapisu historii: {e}')

# Klasa główna aplikacji
class ClockApp:
    def __init__(self):
        self.display_active = False
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.history = HistoryManager.load()

    def display_time(self, stop_event):
        """Wyświetla aktualny czas do momentu zatrzymania."""
        self.display_active = True
        try:
            while not stop_event.is_set():
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"\r{current_time} (naciśnij Enter aby wrócić do menu)", end="")
                time.sleep(1)
        except Exception as e:
            LoggerSingleton.log_error(f'Błąd w display_time: {e}')
        self.display_active = False

    def set_alarm(self, alarm_hour, alarm_minute):
        """Ustawia alarm na podaną godzinę i minutę."""
        try:
            now = datetime.datetime.now()
            alarm_datetime = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
            if alarm_datetime < now:
                alarm_datetime += datetime.timedelta(days=1)
            time_until_alarm = (alarm_datetime - now).total_seconds()
            if time_until_alarm <= 0:
                print("Wybrany czas alarmu jest już przeszły.")
                return
            self.scheduler.enter(time_until_alarm, 1, lambda: print(f"\nAlarm!"))
            mins, secs = divmod(time_until_alarm, 60)
            print(f"Czas do alarmu: {int(mins):02d}:{int(secs):02d}")
            HistoryManager.save({
                'typ': 'alarm',
                'godzina': f'{alarm_hour:02d}:{alarm_minute:02d}',
                'ustawiono': now.strftime('%Y-%m-%d %H:%M:%S')
            })
            self.scheduler.run()
        except Exception as e:
            LoggerSingleton.log_error(f'Błąd w set_alarm: {e}')
            print(f"Błąd: {e}")

    def set_timer(self, timer_duration):
        """Ustawia timer na podany czas w formacie MM:SS."""
        try:
            minutes, seconds = map(int, timer_duration.split(":"))
            total_seconds = minutes * 60 + seconds
            while total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)
                print(f"\r{mins:02d}:{secs:02d}", end="")
                time.sleep(1)
                total_seconds -= 1
            print("\nTimer done!")
            HistoryManager.save({
                'typ': 'timer',
                'czas': timer_duration,
                'ustawiono': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        except Exception as e:
            LoggerSingleton.log_error(f'Błąd w set_timer: {e}')
            print(f"Błąd: {e}")

    def show_history(self):
        """Wyświetla historię alarmów i timerów."""
        try:
            history = HistoryManager.load()
            if not history:
                print("Brak zapisanej historii.")
                return
            print("\n***** HISTORIA *****")
            for entry in history[-10:]:
                if entry['typ'] == 'alarm':
                    print(f"Alarm: {entry['godzina']} (ustawiono: {entry['ustawiono']})")
                elif entry['typ'] == 'timer':
                    print(f"Timer: {entry['czas']} (ustawiono: {entry['ustawiono']})")
            print("********************\n")
        except Exception as e:
            LoggerSingleton.log_error(f'Błąd w show_history: {e}')
            print(f"Błąd: {e}")

class ClockAppGUI:
    def __init__(self, root, logic_app):
        self.root = root
        self.app = logic_app
        self.root.title("Clock, Alarm, Timer - Adrian Lesniak")
        self.root.geometry("1400x900")  # jeszcze większe okno
        self.root.minsize(1400, 900)
        self.root.configure(bg="#f7f7f2")
        self.create_widgets()
        self._alarm_thread = None
        self._timer_thread = None
        self._alarm_queue = queue.Queue()
        self._timer_queue = queue.Queue()
        self._alarm_running = False
        self._timer_running = False

    def create_widgets(self):
        # Usunięte logo
        # Centered description
        desc = ("Clock application:\n"
                "- Clock: shows current time\n"
                "- Alarm: set an alarm\n"
                "- Timer: countdown\n"
                "- History: last alarms/timers\n"
                "\nAuthor: Adrian Lesniak")
        label_desc = tk.Label(self.root, text=desc, bg="#f7f7f2", fg="#1a237e", font=("Arial", 15, "bold"), justify="center")
        label_desc.pack(pady=(10, 0), anchor="center", padx=50)

        tk.Label(self.root, text="★"*80, fg="#ffb300", bg="#f7f7f2", font=("Arial", 16)).pack(pady=(10, 0))
        ttk.Separator(self.root, orient='horizontal').pack(fill='x', padx=40, pady=10)

        btn_frame = tk.Frame(self.root, bg="#f7f7f2")
        btn_frame.pack(pady=10)
        btn1 = tk.Button(btn_frame, text="🕒 Show current time", command=self.show_time, bg="#e3f2fd", fg="#0d47a1", font=("Arial", 13, "bold"), width=24, height=1)
        btn2 = tk.Button(btn_frame, text="⏰ Set alarm", command=self.set_alarm, bg="#fffde7", fg="#f57c00", font=("Arial", 13, "bold"), width=24, height=1)
        btn3 = tk.Button(btn_frame, text="⏳ Set timer", command=self.set_timer, bg="#e8f5e9", fg="#388e3c", font=("Arial", 13, "bold"), width=24, height=1)
        btn4 = tk.Button(btn_frame, text="📜 History", command=self.show_history, bg="#fce4ec", fg="#ad1457", font=("Arial", 13, "bold"), width=24, height=1)
        btn5 = tk.Button(btn_frame, text="❌ Exit", command=self.root.quit, bg="#ffebee", fg="#b71c1c", font=("Arial", 13, "bold"), width=24, height=1)
        btn1.grid(row=0, column=0, pady=6)
        btn2.grid(row=0, column=1, pady=6, padx=10)
        btn3.grid(row=0, column=2, pady=6, padx=10)
        btn4.grid(row=0, column=3, pady=6, padx=10)
        btn5.grid(row=0, column=4, pady=6, padx=10)

        ttk.Separator(self.root, orient='horizontal').pack(fill='x', padx=40, pady=14)
        tk.Label(self.root, text="★"*80, fg="#ffb300", bg="#f7f7f2", font=("Arial", 16)).pack()

        self.content_frame = tk.Frame(self.root, bg="#f7f7f2", relief="groove", bd=2)
        self.content_frame.pack(fill="both", expand=True, padx=50, pady=20)
        self.content_label = tk.Label(self.content_frame, text="Welcome! Select an option above.", bg="#f7f7f2", fg="#263238", font=("Arial", 26), justify="center")
        self.content_label.pack(expand=True)
        self.time_running = False

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_time(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="", font=("Arial", 90, "bold"), bg="#e3f2fd", fg="#0d47a1")
        label.pack(pady=60)
        self.time_running = True
        def update_time():
            if not self.time_running or not label.winfo_exists():
                return
            label.config(text=datetime.datetime.now().strftime("%H:%M:%S"))
            self.content_frame.after(1000, update_time)
        update_time()

    def set_alarm(self):
        self.clear_content()
        alarm_frame = tk.Frame(self.content_frame, bg="#fffde7", bd=3, relief="ridge")
        alarm_frame.pack(pady=60, padx=60)
        tk.Label(alarm_frame, text="Set Alarm", font=("Arial", 28, "bold"), bg="#fffde7", fg="#f57c00").pack(pady=(10, 20))
        form = tk.Frame(alarm_frame, bg="#fffde7")
        form.pack(pady=10)
        tk.Label(form, text="Hour:", bg="#fffde7", font=("Arial", 18)).grid(row=0, column=0, padx=10, pady=10)
        entry_hour = tk.Entry(form, width=6, font=("Arial", 18))
        entry_hour.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(form, text="Minute:", bg="#fffde7", font=("Arial", 18)).grid(row=0, column=2, padx=10, pady=10)
        entry_minute = tk.Entry(form, width=6, font=("Arial", 18))
        entry_minute.grid(row=0, column=3, padx=10, pady=10)
        result_label = tk.Label(alarm_frame, text="", bg="#fffde7", font=("Arial", 16))
        result_label.pack(pady=10)
        self.alarm_status_label = tk.Label(alarm_frame, text="", bg="#fffde7", font=("Arial", 22, "bold"))
        self.alarm_status_label.pack(pady=10)
        def set_alarm_action():
            try:
                hour = int(entry_hour.get())
                minute = int(entry_minute.get())
                if not (0 <= hour <= 23 and 0 <= minute <= 59):
                    raise ValueError
                self._alarm_running = True
                self._alarm_queue = queue.Queue()
                self._alarm_thread = threading.Thread(target=self._alarm_countdown, args=(hour, minute, self._alarm_queue))
                self._alarm_thread.start()
                self._update_alarm_gui()
            except Exception:
                result_label.config(text="Invalid input! Enter hour 0-23 and minute 0-59.", fg="#b71c1c")
        btn = tk.Button(alarm_frame, text="Set alarm", command=set_alarm_action, bg="#f57c00", fg="#fffde7", font=("Arial", 18, "bold"), width=16, height=1)
        btn.pack(pady=15)

    def _alarm_countdown(self, hour, minute, q):
        now = datetime.datetime.now()
        alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if alarm_time < now:
            alarm_time += datetime.timedelta(days=1)
        total_seconds = int((alarm_time - now).total_seconds())
        while total_seconds > 0 and self._alarm_running:
            mins, secs = divmod(total_seconds, 60)
            q.put(f"Alarm in {mins:02d}:{secs:02d}")
            time.sleep(1)
            total_seconds -= 1
        if self._alarm_running:
            q.put("ALARM! Time is up!")
            HistoryManager.save({
                'typ': 'alarm',
                'godzina': f'{hour:02d}:{minute:02d}',
                'ustawiono': now.strftime('%Y-%m-%d %H:%M:%S')
            })
        self._alarm_running = False

    def _update_alarm_gui(self):
        try:
            msg = self._alarm_queue.get_nowait()
            self.alarm_status_label.config(text=msg, fg="#388e3c" if "ALARM" in msg else "#0d47a1")
        except queue.Empty:
            pass
        if self._alarm_running:
            self.root.after(200, self._update_alarm_gui)
        else:
            self.alarm_status_label.config(text="Alarm finished!", fg="#388e3c")

    def set_timer(self):
        self.clear_content()
        timer_frame = tk.Frame(self.content_frame, bg="#e8f5e9", bd=3, relief="ridge")
        timer_frame.pack(pady=60, padx=60)
        tk.Label(timer_frame, text="Set Timer", font=("Arial", 28, "bold"), bg="#e8f5e9", fg="#388e3c").pack(pady=(10, 20))
        form = tk.Frame(timer_frame, bg="#e8f5e9")
        form.pack(pady=10)
        tk.Label(form, text="Time (MM:SS):", bg="#e8f5e9", font=("Arial", 18)).grid(row=0, column=0, padx=10, pady=10)
        entry_timer = tk.Entry(form, width=10, font=("Arial", 18))
        entry_timer.grid(row=0, column=1, padx=10, pady=10)
        result_label = tk.Label(timer_frame, text="", bg="#e8f5e9", font=("Arial", 16))
        result_label.pack(pady=10)
        self.timer_status_label = tk.Label(timer_frame, text="", bg="#e8f5e9", font=("Arial", 22, "bold"))
        self.timer_status_label.pack(pady=10)
        def set_timer_action():
            try:
                timer = entry_timer.get()
                minutes, seconds = map(int, timer.split(":"))
                if minutes < 0 or seconds < 0 or seconds > 59:
                    raise ValueError
                self._timer_running = True
                self._timer_queue = queue.Queue()
                self._timer_thread = threading.Thread(target=self._timer_countdown, args=(minutes, seconds, self._timer_queue))
                self._timer_thread.start()
                self._update_timer_gui()
            except Exception:
                result_label.config(text="Invalid format! Use MM:SS.", fg="#b71c1c")
        btn = tk.Button(timer_frame, text="Start timer", command=set_timer_action, bg="#388e3c", fg="#e8f5e9", font=("Arial", 18, "bold"), width=16, height=1)
        btn.pack(pady=15)

    def _timer_countdown(self, minutes, seconds, q):
        total_seconds = minutes * 60 + seconds
        while total_seconds >= 0 and self._timer_running:
            m, s = divmod(total_seconds, 60)
            q.put(f"{m:02d}:{s:02d}")
            time.sleep(1)
            total_seconds -= 1
        if self._timer_running:
            q.put("Timer done!")
            HistoryManager.save({
                'typ': 'timer',
                'czas': f'{minutes:02d}:{seconds:02d}',
                'ustawiono': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        self._timer_running = False

    def _update_timer_gui(self):
        try:
            msg = self._timer_queue.get_nowait()
            self.timer_status_label.config(text=msg, fg="#388e3c" if "done" in msg else "#388e3c")
        except queue.Empty:
            pass
        if self._timer_running:
            self.root.after(200, self._update_timer_gui)
        else:
            self.timer_status_label.config(text="Timer finished!", fg="#388e3c")

    def show_history(self):
        self.clear_content()
        tk.Label(self.content_frame, text="History (last 10):", font=("Arial", 16, "bold"), bg="#f7f7f2").pack(pady=10)
        history = HistoryManager.load()
        text = tk.Text(self.content_frame, bg="#fce4ec", fg="#ad1457", font=("Arial", 11), wrap="word", height=12)
        text.pack(expand=True, fill="both", padx=10, pady=10)
        if not history:
            text.insert("end", "No history saved.")
        else:
            for entry in history[-10:]:
                if entry['typ'] == 'alarm':
                    text.insert("end", f"Alarm: {entry['godzina']} (set: {entry['ustawiono']})\n")
                elif entry['typ'] == 'timer':
                    text.insert("end", f"Timer: {entry['czas']} (set: {entry['ustawiono']})\n")
        btn = tk.Button(self.content_frame, text="Back to menu", command=self.create_widgets, bg="#f8bbd0", fg="#ad1457", font=("Arial", 11, "bold"))
        btn.pack(pady=5)

# --- Run GUI ---
if __name__ == "__main__":
    app = ClockApp()
    root = tk.Tk()
    gui = ClockAppGUI(root, app)
    root.mainloop()
