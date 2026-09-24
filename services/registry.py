from services.intel import weather, news_wire, knowledge_vault, signal_intercept
from services.hardware import system_pulse, diagnostics
from services.flavor import encrypted_signal, greeting
from utils import crypto_suite, file_navigator

MODULE_REGISTRY = {
    "weather-local": weather.get_local_weather,
    "weather": weather.get_weather_data,
    "system": system_pulse.get_pulse,
    "hello": greeting.get_greeting,
    "diag": diagnostics.system_manager_report,
    # "signal": encrypted_signal.get_encrypted_signal,
    "news": news_wire.get_headlines,
    # "lesson": knowledge_vault.get_daily_lesson,
    "encrypt": crypto_suite.encrypt_decrypt,
    # "tree": file_navigator.get_tree,
    "signal2": signal_intercept.intercept_signal
}


def get_module_data(command):
    """Fetches data from a module if it exists in the registry."""
    if command in MODULE_REGISTRY:
        return MODULE_REGISTRY[command]()
    return "Unknown command. Signal lost in the void..."
