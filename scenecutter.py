import os
import time

import vesputils as vu
from settings import DIRNAME


def cut_videos() -> None:
    videos = vu.get_names()
    for idx, name in enumerate(videos, 1):

        vu.msg(f"Preparing video {idx} of {len(videos)}...")

        folder_name = name[:-4]
        fpath = f"./{DIRNAME}/{folder_name}"
        vpath = f"./{DIRNAME}/{name}"

        os.system(f"if not exist \"{fpath}\" mkdir \"{fpath}\"")
        os.system(f"scenedetect -i \"{vpath}\" detect-adaptive split-video -o \"{fpath}\"")
        vu.delete(vpath)

        vu.msg(f"Video {idx} of {len(videos)} is done!")

    vu.msg("Job is done!")


if __name__ == "__main__":
    cut_videos()
    input("Press any key to exit...")
