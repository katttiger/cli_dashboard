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
                  "ONLINE" + Fore.CYAN + " | Connection:" + Fore.GREEN + " SECURE\n")

            if (current_view == "main"):
                print(f"{print_first_messages()}")
            else:
                print(Fore.YELLOW +
                      f"Fetching Data stream: {current_view.upper()}...")
                print(f"{Fore.WHITE} \n + {get_module_data(current_view)}")

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


def print_first_messages():
    first_line = f"{Fore.WHITE} Incoming Transmission: {Fore.YELLOW} {get_module_data("hello")}"
    second_line = f"{Fore.WHITE}Atmospheric data: {Fore.MAGENTA} {get_module_data("weather-local")}"
    third_line = f"{Fore.WHITE}Hardware pulse: {Fore.GREEN} {get_module_data("system")}"

    response = f"{first_line} \n {second_line} \n {third_line}"
    return response


if __name__ == "__main__":
    run_dashboard()
