import os
import time


def get_names(path=".", ext=".mp4") -> list:
    return [file for file in os.listdir(path) if file.endswith(ext)]


def clear_name(text: str, chars=" -", repl="_") -> str:
    for char in chars:
        if char in text:
            text = text.replace(char, repl)
    return text.lower()


for name in get_names():
    os.system(f"rename \"{name}\" {clear_name(name)}")

for name in get_names():
    folder_name = name[:-4]
    os.system(f"if not exist {folder_name} mkdir {folder_name}")
    os.system(f"scenedetect -i {name} detect-adaptive split-video -o \"./{folder_name}\"")

input("Press any key to exit...")
