# main.py
import sys
import signal

from core.loader import load_skills
from ui.power_console import start_power_console


def main():
    # 🔹 Load all skills once (single source of truth)
    load_skills()

    # 🔹 Start Power Console UI (blocking)
    try:
        start_power_console()
    except KeyboardInterrupt:
        print("\nShutting down JARVIS...")
        sys.exit(0)


if __name__ == "__main__":
    # 🔒 Clean CTRL+C handling (important on Windows)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
