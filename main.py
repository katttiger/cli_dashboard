import os
import sys
import time
from colorama import init, Fore, Style
from services.registry import get_module_data
init()


def run_dashboard():
    current_view = "main"
    try:
        while True:
            os.system('cls' if os.name == "nt" else 'clear')

            print(Fore.CYAN+Style.BRIGHT +
                  "--- SYSTEM OVERRIDE: COMMAND CENTER ---")
            print(Fore.CYAN + "Status: " + Fore.GREEN +
                  "ONLINE" + Fore.CYAN + " | Connection:" + Fore.GREEN + " Secure\n")

            if (current_view == "main"):

                print(Fore.WHITE + "Incoming Transmission: " +
                      Fore.YELLOW + get_module_data("hello"))
                print(Fore.WHITE+"Atmospheric data: " +
                      Fore.MAGENTA + get_module_data("weather-local"))
                print(Fore.WHITE + "Hardware pulse: " +
                      Fore.GREEN + get_module_data("system"))
            else:
                print(Fore.YELLOW +
                      f"Fetching Data stream: {current_view.upper()}...")
                print(Fore.WHITE + "\n" + get_module_data(current_view))

            print("\n" + Fore.CYAN + "-----------------------------------------")
            user_input = input(Fore.CYAN + "CMD> " +
                               Fore.WHITE).strip().lower()

            if (user_input == ""):
                current_view = "main"
            elif user_input == "/exit":
                raise KeyboardInterrupt
            elif user_input.startswith("/"):
                current_view = user_input[1:]
            else:
                current_view = "main"
    except KeyboardInterrupt:
        print(Fore.RED + "\nSession terminated. Connection lost...")


if __name__ == "__main__":
    run_dashboard()
