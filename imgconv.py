"""
Image convertation module
"""

import glob
import os

import imagesize

from PIL import Image
import vesputils as vu
from settings import IMGJUNKSIZE


def prepare_images() -> None:
    """
    Deletes junk images and converting non-png files to png.
    :return: None
    """
    images = glob.glob(".\\simple_images\\**\\*") or glob.glob(".\\downloads\\**\\*")

    icount = len([i for i in images if "." in i])
    vu.msg(f"Processing {icount} images...")

    ocount = 0
    for idx, path in enumerate(images, 1):

        info = f"image #{idx}, " + path.split("\\")[-1]

        if path.endswith(".svg") or imagesize.get(path) == IMGJUNKSIZE:
            print(f"Deleting junk {info}")
            os.remove(path)

        elif path.endswith(".png"):
            print(f"     Skipping {info}")
            ocount += 1

        else:
            print(f"   Converting {info}")
            with Image.open(path) as img:
                img.save(path.rsplit(".", 1)[0] + ".png", "png")
            os.remove(path)
            ocount += 1

    vu.msg(f"{ocount} images is converted!")


if __name__ == "__main__":
    prepare_images()
    input("Press any key to exit...")
