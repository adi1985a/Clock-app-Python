import time
import datetime
import argparse
import threading
import sched

# Zmienna do kontrolowania uruchomienia wątku display_time
display_active = False


def display_time(stop_event):
    global display_active
    while not stop_event.is_set():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\r{current_time} (naciśnij Enter aby wrócić do menu)", end="")
        time.sleep(1)
    display_active = False


def set_alarm(scheduler, alarm_hour, alarm_minute):
    try:
        now = datetime.datetime.now()
        alarm_datetime = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)

        if alarm_datetime < now:
            alarm_datetime += datetime.timedelta(days=1)  # Alarm na następny dzień jeśli już minął

        time_until_alarm = (alarm_datetime - now).total_seconds()

        if time_until_alarm <= 0:
            print("Wybrany czas alarmu jest już przeszły.")
            return

        # Ustawienie zadania alarmu w schedulera
        scheduler.enter(time_until_alarm, 1, lambda: print(f"\nAlarm!"))

        # Wyświetlenie czasu do alarmu w jednym wierszu
        while time_until_alarm > 0:
            mins, secs = divmod(time_until_alarm, 60)
            time_format = '{:02d}:{:02d}'.format(int(mins), int(secs))
            print(f"\rCzas do alarmu: {time_format} (naciśnij Enter aby wrócić do menu)", end="")
            time.sleep(1)
            time_until_alarm -= 1

        # Oczekiwanie na naciśnięcie Enter przed powrotem do menu
        input("\nNaciśnij Enter, aby wrócić do menu głównego...")

    except ValueError as e:
        print(f"Błąd: {e}")


def set_timer(timer_duration):
    minutes, seconds = map(int, timer_duration.split(":"))
    total_seconds = minutes * 60 + seconds
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\r{time_format}", end="")
        time.sleep(1)
        total_seconds -= 1
    print("\nTimer done!")


def main():
    global display_active
    parser = argparse.ArgumentParser(description="Aplikacja zegarowa z funkcją zegarka, budzika i timera.")
    parser.add_argument('-alarm', action='store_true', help='Ustaw alarm')
    parser.add_argument('-timer', type=str, help='Ustaw timer na podany czas w formacie MM:SS')
    args = parser.parse_args()

    while True:
        if args.alarm:
            try:
                alarm_hour = int(input("Podaj godzinę alarmu (0-23): "))
                if alarm_hour < 0 or alarm_hour > 23:
                    raise ValueError("Godzina musi być w zakresie 0-23.")

                alarm_minute = int(input("Podaj minutę alarmu (0-59): "))
                if alarm_minute < 0 or alarm_minute > 59:
                    raise ValueError("Minuta musi być w zakresie 0-59.")

                # Inicjalizacja schedulera
                scheduler = sched.scheduler(time.time, time.sleep)

                # Uruchomienie alarmu w osobnym wątku
                alarm_thread = threading.Thread(target=set_alarm, args=(scheduler, alarm_hour, alarm_minute))
                alarm_thread.start()

                # Oczekiwanie na naciśnięcie Enter przed powrotem do menu
                input("\nNaciśnij Enter, aby wrócić do menu głównego...")

            except ValueError as e:
                print(f"Błąd: {e}")

        elif args.timer:
            set_timer(args.timer)
            break  # Po zakończeniu timera wracamy od razu do menu

        else:
            print("\nMenu:")
            print("1. Pokaż aktualny czas")
            print("2. Ustaw alarm")
            print("3. Wyjście")
            choice = input("Wybierz opcję (1/2/3): ")

            if choice == '1':
                if not display_active:
                    stop_event = threading.Event()
                    display_thread = threading.Thread(target=display_time, args=(stop_event,))
                    display_thread.start()
                    input("\nNaciśnij Enter, aby wrócić do menu głównego...")
                    stop_event.set()
                    display_thread.join()
                    display_active = False  # Ustaw flagę na false po zakończeniu wątku

            elif choice == '2':
                try:
                    alarm_hour = int(input("Podaj godzinę alarmu (0-23): "))
                    if alarm_hour < 0 or alarm_hour > 23:
                        raise ValueError("Godzina musi być w zakresie 0-23.")

                    alarm_minute = int(input("Podaj minutę alarmu (0-59): "))
                    if alarm_minute < 0 or alarm_minute > 59:
                        raise ValueError("Minuta musi być w zakresie 0-59.")

                    # Inicjalizacja schedulera
                    scheduler = sched.scheduler(time.time, time.sleep)

                    # Uruchomienie alarmu w osobnym wątku
                    alarm_thread = threading.Thread(target=set_alarm, args=(scheduler, alarm_hour, alarm_minute))
                    alarm_thread.start()

                    # Oczekiwanie na naciśnięcie Enter przed powrotem do menu
                    input("\nNaciśnij Enter, aby wrócić do menu głównego...")

                except ValueError as e:
                    print(f"Błąd: {e}")

            elif choice == '3':
                print("Zakończenie programu.")
                break

            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()
