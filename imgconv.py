import glob
import os

import imagesize

from PIL import Image
import vesputils as vu
from settings import IMGJUNKSIZE


def prepare_images() -> None:
    images = glob.glob(".\\simple_images\\**\\*")

    vu.msg(f"Trying to convert {len(images)} images...")

    for idx, path in enumerate(images):

        info = f"image #{idx}, {path[16:]}"

        if imagesize.get(path) == IMGJUNKSIZE:
            print(f"Deleting junk {info}...")
            os.system(f"del {path}")

        elif path.endswith(".png"):
            print(f"Skipping {info}...")

        else:
            print(f"Converting {info}...")
            img = Image.open(path)
            img.save(path.rsplit(".", 1)[0] + ".png", "png")
            os.system(f"del {path}")

    vu.msg(f"All {len(images)} images is converted!")

if __name__ == "__main__":
    prepare_images()
    input("Press any key to exit...")
