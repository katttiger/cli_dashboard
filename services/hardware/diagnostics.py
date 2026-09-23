import psutil
from colorama import Fore, Style


def get_visual_bar(percent, lenth=20):
    filled = int(lenth*percent/100)
    bar = "|"*filled+"-"*(lenth-filled)
    return f"[{bar}] {percent}%"


def get_disk_info():
    usage = psutil.disk_usage('/')
    return f"DISK USAGE: {get_visual_bar(usage.percent)} ({usage.free // (1024**3)}GB Free)"


def get_battery_info():
    battery = psutil.sensors_battery()
    if battery is None:
        return "BATTERY: [NOT DETECTED]"
    percent = battery.percent
    status = "CHARGING" if battery.power_plugged else "DISCHARGING"
    return f"BATTERY: {get_visual_bar(percent)} {status}"


def get_ram_info():
    ram = psutil.virtual_memory()
    return f"RAM LOAD: {get_visual_bar(ram.percent)} ({ram.used // (1024**2)}MB used)"


def get_process_audit():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    sorted_proc = sorted(
        processes, key=lambda x: x['memory_info'].rss, reverse=True)

    report = f"\n{Fore.RED}--- TOP RESOURCE HOGS ---\n"
    for p in sorted_proc[:5]:
        mem_mb = p['memory_info'].rss//(1024*1024)
        report += f"PID: {p['pid']} | {p['name']} | {mem_mb}MB \n"
    return report


def system_manager_report():
    header = (f"{get_ram_info()}\n"
              f"{get_disk_info()}\n"
              f"{get_battery_info()}")
    return f"{header}\n{get_process_audit()}"
