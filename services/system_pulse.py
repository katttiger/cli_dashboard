import psutil


def get_pulse():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory()
    ram_used = round(ram_info.used/(1024**3), 2)
    ram_total = round(ram_info.total/(1024**3), 2)

    return f"CPU: {cpu_usage}% | RAM: {ram_used} GB / {ram_total} GB"
