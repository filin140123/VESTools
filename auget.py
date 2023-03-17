"""
Getting audio from video file
"""

import glob
import os

import vesputils as vu
from settings import DIRNAME, AUDIRNAME


def get_audio() -> None:
    """
    Extracts audio from one or multiple video files
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
                name = file.split("\\")[-1]
                output = f"./{AUDIRNAME}/audio_{name[:-4]}.mp3"

                vu.msg(f"\nExtracting audio, file {idx} of {len(files)}...\n")
                os.system(f"ffmpeg -i \"{file}\" -q:a 0 -map a \"{output}\"")
            break
        elif int(choice) in range(1, len(files)+1):
            file = files[int(choice)-1]
            name = file.split("\\")[-1]
            output = f"./{AUDIRNAME}/audio_{name[:-4]}.mp3"

            vu.msg(f"\nExtracting audio from {name}...\n")
            os.system(f"ffmpeg -i \"{file}\" -q:a 0 -map a \"{output}\"")
            break
        else:
            vu.msg("Wrong index, try again...")

    vu.msg("\nAudio extracted!\n")


if __name__ == "__main__":
    get_audio()
    input("Press any key to exit...")
