import os

import vesputils as vu
from settings import DIRNAME


def cut_videos(videos: list) -> None:
    """
    :param videos: List of paths to videos
    :return: None
    """
    for idx, video in enumerate(videos, 1):
        vu.msg(f"Preparing video {idx} of {len(videos)}...")

        scene_dir = video[:-4]
        vu.dircheck(scene_dir)
        os.system(f"scenedetect -i \"{video}\" detect-adaptive split-video -o \"{scene_dir}\"")
        os.remove(video)

        vu.msg(f"Video {idx} of {len(videos)} is done!")

    vu.msg("Job is done!")


if __name__ == "__main__":
    cut_videos([file for file in os.listdir(DIRNAME) if file.endswith(".mp4")])
    input("Press any key to exit...")
