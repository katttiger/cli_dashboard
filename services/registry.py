from services.intel import weather
from services.hardware import system_pulse, diagnostics
from services.flavor import encrypted_signal, greeting

MODULE_REGISTRY = {
    "weather": weather.get_weather,
    "system": system_pulse.get_pulse,
    "hello": greeting.get_greeting,
    "diag": diagnostics.get_full_diagnostics,
    "signal": encrypted_signal.get_encrypted_signal,
}


def get_module_data(command):
    """Fetches data from a module if it exists in the registry."""
    if command in MODULE_REGISTRY:
        return MODULE_REGISTRY[command]()
    return "Unknown command. Signal lost in the void..."
