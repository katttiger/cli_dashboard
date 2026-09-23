from services.intel import weather, news_wire, knowledge_vault, crypto_suite
from services.hardware import system_pulse, diagnostics
from services.flavor import encrypted_signal, greeting

MODULE_REGISTRY = {
    "weather": weather.get_weather,
    "system": system_pulse.get_pulse,
    "hello": greeting.get_greeting,
    "diag": diagnostics.get_full_diagnostics,
    "signal": encrypted_signal.get_encrypted_signal,
    "news": news_wire.get_headlines,
    "lesson": knowledge_vault.get_daily_lesson,
    "encrypt": crypto_suite.encrypt_decrypt
}


def get_module_data(command):
    """Fetches data from a module if it exists in the registry."""
    if command in MODULE_REGISTRY:
        return MODULE_REGISTRY[command]()
    return "Unknown command. Signal lost in the void..."
