import os
import time
from services import greeting, weather, system_pulse


def run_dashboard():
    try:
        while True:
            os.system('cls' if os.name == "nt" else 'clear')
            print("--- Welcome to your LIVE CLI Dashboard ---")
            print(f"Status: Monitoring... (Press Ctrl+C to exit)\n")

            print(greeting.get_greeting())
            print(weather.get_weather())
            print(system_pulse.get_pulse())

            print("\n-----------------------------------------")

            time.sleep(5)
    except KeyboardInterrupt:
        print("\nDashboard shut down. Goodbye!")


if __name__ == "__main__":
    run_dashboard()
