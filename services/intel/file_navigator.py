import os
from colorama import Fore, Style


def get_tree(root_dir="."):
    output = f"{Fore.CYAN}SCANNING DIRECTORY STRUCTURE...{Style.RESET_ALL}\n"
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').strip('/')
        indent = ' ' * 4 * (level.count('/') + 1)
        output += f"{Fore.GREEN}{'/' if level else 'Root'}{Style.RESET_ALL}\n"
        # Simplified tree view for the CLI
        for d in dirs:
            output += f"{indent}└── {Fore.YELLOW}{d}{Style.RESET_ALL}\n"
        for f in files:
            output += f"{indent}── {Fore.WHITE}{f}{Style.RESET_ALL}\n"
    return output
