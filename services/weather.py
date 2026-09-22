import requests


def get_weather():
    try:
        response = requests.get("https://wttr.in?format=3")
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Weather data currently unavailable."
    except Exception as e:
        return (f"Connection error: {e}")
