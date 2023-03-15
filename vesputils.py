"""
Utilities for scripts. Not for use.
"""

import os
import time


def clear_name(text: str, fchars: str = "|:<>/*?\\\"+", gaps: str = " -,&", repl: str = "_") -> str:
    """
    Removes forbidden characters from string and replaces whitespaces with specified symbol
    :param text: string to clean
    :param fchars: string of forbidden characters
    :param gaps: string of characters to replace with repl
    :param repl: specified symbol to replace gaps with
    :return: clear string
    """
    for char in fchars:
        if char in text:
            text = text.replace(char, "")
    for char in gaps:
        if char in text:
            text = text.replace(char, repl)
    return text.lower()


def get_amount(value: str, default: int) -> int:
    """
    Make sure value is int and more than 0. Otherwise returns default value.
    :param value: raw string input
    :param default: default integer value
    :return: user value or default value, depends on input
    """
    try:
        value = int(value)
        return value if value > 0 else default
    except ValueError:
        return default


def msg(message: str) -> None:
    """
    Prints a message with 0.5 second pause
    :param message: Text to print
    :return: None
    """
    print(message)
    time.sleep(0.5)


def countdown(n: int) -> None:
    """
    Counting down from n to zero
    :param n: Seconds to zero
    :return: None
    """
    for i in range(n, 0, -1):
        print(f"{i}... ", end="\r")
        time.sleep(1)


def dircheck(dirname: str) -> None:
    """
    Creates directory if it not exist already
    :param dirname: Directory name you want to create
    :return: None
    """
    os.system(f"if not exist {dirname} mkdir {dirname}")


if __name__ == "__main__":
    msg("This file is not for use...")
    msg("Exiting...")
