# cli_utils.py

import time
import os
import sys


def clear_screen():
    """
    Clear the terminal screen.

    Makes output cleaner when switching sections.
    Works on both Windows and Unix systems.
    """
    os.system("cls" if os.name == "nt" else "clear")


def clear_line(n: int = 1):
    """
    Clear the previous N lines in the terminal.

    Parameters:
        n (int): Number of lines to erase. Useful for animations.

    Uses basic ANSI escape codes:
        - \033[1A → move cursor up by one line
        - \033[2K → clear the entire current line
    """
    for _ in range(n):
        sys.stdout.write("\033[1A")     # Move cursor up
        sys.stdout.write("\r\033[2K")   # Clear line
    sys.stdout.flush()


def anim(r: int = 2, text: str = '\rLoading', sec: float = 0.5):
    """
    Show a simple loading animation.

    Parameters:
        r (int): Number of pulse cycles. Each cycle prints 1–3 dots.
        text (str): Text shown before the dots.
        sec (float): Delay between frames.

    This is mainly for visual effect so users know “something is happening”.
    """
    clear_screen()  # Always start with a clean slate

    for _ in range(r):
        for dots in range(1, 4):
            sys.stdout.write(f"{text}{'.' * dots}")
            sys.stdout.flush()
            time.sleep(sec)

    # Remove the animation text from screen
    clear_line()