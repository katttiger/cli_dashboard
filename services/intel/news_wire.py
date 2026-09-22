import feedparser
import requests


def get_headlines():
    # Let's try the New York Times world feed as a test
    rss_url = "https://www.aftonbladet.se/rss.xml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.443.0 Safari 537.36'
    }

    try:
        response = requests.get(rss_url, headers=headers, timeout=10)
        # DEBUG: Print the status code to the console
        # print(f"DEBUG: Server responded with {response.status_code}")

        feed = feedparser.parse(response.content)

        if not feed.entries:
            return "GLOBAL INTEL: [SIGNAL WEAK - NO DATA RETRIEVED]"

        headlines = [entry.title for entry in feed.entries[:3]]
        formatted_news = "\n".join([f" >> {h}" for h in headlines])
        return f"GLOBAL INTEL:\n{formatted_news}"

    except Exception as e:
        return f"SIGNAL LOST: Unable to intercept global news wire. \nError: {e}"
