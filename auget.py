"""
Getting audio from video file
"""

import glob
import os

import vesputils as vu
from settings import DIRNAME, AUDIRNAME


def extract(fp, num=None) -> None:
    """
    Extracts audio from file
    :param fp: path to file
    :param num: list of current video and total number of videos, for multiple videos
    :return: None
    """
    name = fp.split("\\")[-1]
    output = f"./{AUDIRNAME}/audio_{name[:-4]}.mp3"
    if num:
        vu.msg(f"\nExtracting audio, file {num[0]} of {num[1]}...\n")
    else:
        vu.msg(f"\nExtracting audio from {name}...\n")
    os.system(f"ffmpeg -i \"{fp}\" -q:a 0 -map a \"{output}\"")


def get_audio() -> None:
    """
    Setup for audio extraction
    :return: None
    """
    files = glob.glob(f".\\{DIRNAME}\\*")

    while True:
        for idx, elem in enumerate(files, 1):
            print(f"#{idx}: " + elem.split("\\")[-1])

        choice = input("Choose file by number or enter \"all\": ")

        os.system(f"if not exist {AUDIRNAME} mkdir {AUDIRNAME}")

        if choice in ("all", "ALL", "All", "a", "A"):
            for idx, file in enumerate(files, 1):
                extract(file, [idx, len(files)])
            break
        elif int(choice) in range(1, len(files)+1):
            extract(files[int(choice)-1])
            break
        else:
            vu.msg("Wrong index, try again...")

    vu.msg("\nAudio extracted!\n")


if __name__ == "__main__":
    get_audio()
    input("Press any key to exit...")
