import random


def get_greeting():
    greetings = [
        "Good morning, Captain! The systems are nominal.",
        "Welcome back. The digital realm missed you.",
        "Greetings! Ready to conquer the day's tasks?",
        "Hello! Your dashboard is primed and ready for action.",
        "Welcome back to the bridge. All systems go!"
    ]

    return random.choice(greetings)
