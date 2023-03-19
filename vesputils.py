"""
Utilities for scripts. Not for use.
"""

import time
from settings import IMGDEFCOUNT


def clear_name(text: str, fchars="|:<>/*?\\\"+", gaps=" -—,&", repl="_") -> str:
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
    while True:
        if "__" in text:
            text = text.replace("__", repl)
        else:
            break
    result = text.lower()
    return result


def get_amount(value: str, default=IMGDEFCOUNT) -> int:
    """
    Make sure value is int and more than 0. Otherwise returns default value.
    :param value: raw string input
    :param default: default integer value
    :return: user value or default value, depends on input
    """
    try:
        value = int(value)
        return value if value > 0 else default
    except (TypeError, ValueError):
        return default


def msg(message: str, seconds=0.5, refresh=False) -> None:
    """
    Prints a message with 0.5 second pause
    :param message: Text to print, str
    :param seconds: Seconds to wait, can be int or float
    :param refresh: Erase output after waiting? True or False
    :return: None
    """
    print(message, end="\r" if refresh else "\n")
    time.sleep(seconds)


def countdown(waitfor: int) -> None:
    """
    Counting down from n to zero
    :param waitfor: Seconds to zero
    :return: None
    """
    for i in range(waitfor, 0, -1):
        msg(f"{i}... ", seconds=1, refresh=True)


if __name__ == "__main__":
    msg("This file is not for use...")
    msg("Exiting...")
