import requests
from colorama import Fore


def get_local_weather():
    try:
        response = requests.get("https://wttr.in?format=3")
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Weather data currently unavailable."
    except Exception as e:
        return (f"Connection error: {e}")


def get_weather_data():
    try:
        response = requests.get("https://wttr.in")
        if response.status_code == 200:
            data = response.text
            return (f"{Fore.MAGENTA}--- [ SECTOR ENVIRONMENTAL ANALYSIS ] ---\n\n"
                    f"{Fore.WHITE}{data}\n"
                    f"{Fore.MAGENTA}--- [ END OF TRANSMISSION ] ---")
        else:
            return " [ ERROR ] Satellite link unstable. Unable to retrieve deep scan."
    except Exception as e:
        return f" [ CONNECTION FAILURE ] : {e}"
