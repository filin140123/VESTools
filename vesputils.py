# Functions and data library. Not for use.
import os
import time

from settings import DIRNAME


def clear_name(text: str, fchars="|:<>/*?\\\"+", gaps=" -,&", repl="_") -> str:
    for char in fchars:
        if char in text:
            text = text.replace(char, "")
    for char in gaps:
        if char in text:
            text = text.replace(char, repl)
    return text.lower()


def get_names(path=f"./{DIRNAME}", ext=".mp4") -> list:
    return [file for file in os.listdir(path) if file.endswith(ext)]


def msg(message: str) -> None:
    print(message)
    time.sleep(0.5)


def countdown(n: int) -> None:
    for i in range(n, 0, -1):
        print(f"{i}... ", end="\r")
        time.sleep(1)


if __name__ == "__main__":
	clear_name(text, fchars, gaps, repl)
	get_names(path, ext)
	msg(message)
    countdown(n)
