"""
Getting images, old version
"""

import os
import shutil
import http
import requests

import imgconv
import vesputils as vu
from settings import IMGDIRNAME
from simple_image_download.simple_image_download import Downloader


user_req = input("Enter your requests divided by comma: ")
user_cnt = input("How many images do you need?: ")

img_count = vu.get_amount(user_cnt)
clear_req = user_req.replace(" ", "+").replace(",+", " ")

vu.msg(f"Trying to download {img_count} images for each request...")

for i in range(1, 11):
    try:
        Downloader().download(clear_req, limit=img_count)
    except (http.client.IncompleteRead, requests.exceptions.ConnectionError):
        vu.msg(f"Server or parsing problems, try #{i} has failed...")
        vu.msg("Trying again in 5 seconds...")
        vu.countdown(5)
    else:
        break
else:
    vu.msg("Download failed 10 times. Exiting...")
    quit()

imgconv.prepare_images()  # Converting images and deleting junk files

vu.dircheck(IMGDIRNAME)
os.system(f"xcopy /s /y /q simple_images {IMGDIRNAME} > nul")
shutil.rmtree(os.path.abspath("simple_images"))

vu.msg("Job is done!")

input("Press any key to exit...")
