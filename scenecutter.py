import os
import time

import vesputils as vu
from settings import DIRNAME


def cut_videos() -> None:
    for name in vu.get_names():
        folder_name = name[:-4]
        fpath = f"./{DIRNAME}/{folder_name}"
        vpath = f"./{DIRNAME}/{name}"
        os.system(f"if not exist \"{fpath}\" mkdir \"{fpath}\"")
        os.system(f"scenedetect -i \"{vpath}\" detect-adaptive split-video -o \"{fpath}\"")


if __name__ == "__main__":
    cut_videos()
    input("Press any key to exit...")
