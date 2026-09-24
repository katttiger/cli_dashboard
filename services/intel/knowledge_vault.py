import requests
import random
from colorama import Fore


def get_daily_lesson():
    classifications = [
        (Fore.RED, "S-CLASS"),
        (Fore.YELLOW, "A-CLASS"),
        (Fore.CYAN, "B-CLASS"),
        (Fore.WHITE, "C-CLASS"),
    ]

    headers = {
        'User-Agent': 'MyCoolDashboard/1.0 (https://github.com/example/project)'
    }

    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            title = data.get("title", "Unknonw subject")
            extract = data.get("extract", "Data corrupted or redacted.")

            if len(extract) > 250:
                extract = extract[:247] + "..."
            color, label = random.choice(classifications)

            return (
                f"{color}--- [ INTEL BRIEF: {label} ] ---\n"
                f"{Fore.WHITE}SUBJECT: {Fore.GREEN}{title}\n"
                f"{Fore.WHITE}DATA: {Fore.WHITE}{extract}\n"
                f"{color}----------------------------"
            )
        else:
            return f"{Fore.RED}VAULT ERROR: Connection to archives timed out."

    except Exception as e:
        return f"{Fore.RED}CRITICAL FAILURE: Vault access denied. \nError: {e}"
