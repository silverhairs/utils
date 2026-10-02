#!/usr/bin/env python3
"""
Microsoft Teams Keep Active Script

This script prevents Microsoft Teams from marking you as idle by
simulating subtle mouse movements at regular intervals.

Usage:
    python teams_keep_active.py [--interval SECONDS]

Options:
    --interval SECONDS    Time between mouse movements (default: 240 seconds / 4 minutes)
    --help               Show this help message

Requirements:
    - pyautogui: pip install pyautogui
    - For macOS: pip install pyobjc-core pyobjc

Press Ctrl+C to stop the script.
"""

import argparse
import time
import sys
from datetime import datetime

try:
    import pyautogui
except ImportError:
    print("Error: pyautogui is not installed.")
    print("Please install it using: pip install pyautogui")
    if sys.platform == "darwin":
        print("On macOS, also install: pip install pyobjc-core pyobjc")
    sys.exit(1)


def move_mouse_slightly():
    """Move the mouse cursor by 1 pixel and then back to simulate activity."""
    try:
        # Get current mouse position
        current_x, current_y = pyautogui.position()

        # Move mouse by 1 pixel
        pyautogui.moveRel(1, 0, duration=0.1)

        # Move back to original position
        pyautogui.moveRel(-1, 0, duration=0.1)

        return True
    except Exception as e:
        print(f"Error moving mouse: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Keep Microsoft Teams active by simulating mouse movements"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=240,
        help="Time between mouse movements in seconds (default: 240 / 4 minutes)",
    )

    args = parser.parse_args()

    if args.interval < 30:
        print("Warning: Interval less than 30 seconds might be too frequent.")
        print("Teams typically marks users idle after 5 minutes of inactivity.")

    print(f"Teams Keep Active Script Started")
    print(f"Interval: {args.interval} seconds ({args.interval/60:.1f} minutes)")
    print(f"Press Ctrl+C to stop\n")

    # Disable fail-safe (moving mouse to corner won't stop the script)
    pyautogui.FAILSAFE = False

    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if move_mouse_slightly():
                print(f"[{timestamp}] Mouse moved - keeping Teams active ✓")
            else:
                print(f"[{timestamp}] Failed to move mouse ✗")

            time.sleep(args.interval)

    except KeyboardInterrupt:
        print("\n\nScript stopped by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
