import requests
import random
from colorama import Fore, Style


def intercept_signal():
    signals = [
        ("ADVICE", "https://api.adviceslip.com/advice"),
        ("FACT", "https://catfact.ninja/fact"),  # Example of a random fact API
        ("QUOTE", "https://zen-quotes.info/api/quotes/random")
    ]

    label, url = random.choice(signals)
    header = f"{Fore.MAGENTA}[INTERCEPTING SIGNAL: {label}]..."

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if label == "ADVICE":
            content = data.get('slip', {}).get('advice', "Signal lost...")
        elif label == "FACT":
            content = data.get('fact', "Signal lost...")
        elif label == "QUOTE":
            content = data[0].get(
                'q', "Signal lost...") if data else "Signal lost..."
        else:
            content = "Unknown signal source."

        return f"{header}{Fore.CYAN} \nDATA RECOVERED: {content}"
    except Exception as e:
        return f"{header}{Fore.RED}SIGNAL INTERFERENCE: {e}"
