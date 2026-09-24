import feedparser
import requests
import time
import random
from colorama import Fore, Style


def get_headlines():
    rss_url = "https://www.aftonbladet.se/rss.xml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.443.0 Safari 537.36'
    }

    clearances = ["[LEVEL 1]", "[LEVEL 4]", "[TOP SECRET]", "[CLASSIFIED]"]

    try:

        intercept_sequence = f"{Fore.YELLOW}ESTABLISHING LINK... {Fore.GREEN}SUCCESS\n{Fore.YELLOW}DECRYPTING PACKET... {Fore.GREEN}OK\n"
        time.sleep(5)
        response = requests.get(rss_url, headers=headers, timeout=10)
        feed = feedparser.parse(response.content)

        if not feed.entries:
            return f"{intercept_sequence}{Fore.RED}GLOBAL INTEL: [SIGNAL WEAK - NO DATA RETRIEVED]"

        headlines = [entry.title for entry in feed.entries[:10]]
        formatted_news = []
        for h in headlines:
            clearance = random.choice(clearances)
            formatted_news.append(
                f"{Fore.YELLOW}{clearance} {Fore.WHITE} ➔  {h}")

        news_body = "\n".join(formatted_news)
        return f"{intercept_sequence}{Fore.CYAN}--- [ INTERCEPTED GLOBAL INTEL ] ---\n{news_body}\n{Fore.CYAN}--- [ END OF STREAM ] ---"

    except Exception as e:
        return f"{Fore.red}SIGNAL LOST: Unable to intercept global news wire. \nError: {e}"
