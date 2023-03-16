"""
Getting images module
"""

import os
import shutil

from google_images_download import google_images_download

import imgconv
import vesputils as vu
from settings import IMGDIRNAME


response = google_images_download.googleimagesdownload()

user_request = input("Enter your requests divided by comma: ")
user_amount = input("How many images do you need?: ")

img_amount = vu.get_amount(user_amount)

vu.msg(f"Trying to download {img_amount} images for each request...")

response.download({"keywords": user_request, "limit": img_amount})

imgconv.prepare_images()  # Converting images and deleting junk files

os.system(f"if not exist {IMGDIRNAME} mkdir {IMGDIRNAME}")
os.system(f"xcopy /s /y /q downloads {IMGDIRNAME} > nul")
shutil.rmtree(os.path.abspath("downloads"))

vu.msg("Job is done!")

input("Press any key to exit...")
