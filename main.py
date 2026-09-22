import os
import time
from colorama import init, Fore, Style
from services import greeting, weather, system_pulse

init()


def run_dashboard():
    try:
        while True:
            os.system('cls' if os.name == "nt" else 'clear')
            print(Fore.CYAN+Style.BRIGHT +
                  "--- Welcome to your LIVE CLI Dashboard ---")
            print(Fore.CYAN + "Status: " + Fore.GREEN +
                  "ONLINE" + Fore.CYAN + " | Connection:" + Fore.GREEN + " Secure\n")

            print(Fore.WHITE + "Incoming Transmission: " +
                  Fore.YELLOW + greeting.get_greeting())
            print(Fore.WHITE+"Atmospheric data: " +
                  Fore.MAGENTA + weather.get_weather())
            print(Fore.WHITE + "Hardware pulse: " +
                  Fore.GREEN + system_pulse.get_pulse())

            print("\n" + Fore.CYAN + "-----------------------------------------")
            print(Fore.WHITE + "Press Ctrl+C to terminate session")

            time.sleep(5)
    except KeyboardInterrupt:
        print(Fore.RED + "\nSession terminated. Connection lost...")


if __name__ == "__main__":
    run_dashboard()
