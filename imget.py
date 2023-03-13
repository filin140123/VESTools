import os
import http
import requests

from PIL import Image, UnidentifiedImageError
import simple_image_download.simple_image_download as idl
import vesputils as vu
from imgconv import prepare_images
from settings import IMGDIRNAME, IMGDEFCOUNT

user_req = input("Enter your requests divided by comma: ")
user_cnt = input("How many images do you need?: ")

img_count = vu.get_amount(user_cnt, IMGDEFCOUNT)
clear_req = user_req.replace(" ", "+").replace(",+", " ")

vu.msg(f"Trying to download {img_count} images for each request...")

downloader = idl.Downloader()

flag = True
while flag:
    try:
        downloader.download(clear_req, limit=img_count)
        flag = False
    except (http.client.IncompleteRead, requests.exceptions.ConnectionError):
        vu.msg("Server or parsing problems...")
        vu.msg("Trying again in 5 seconds...")
        vu.countdown(5)

prepare_images()  # Converting images and deleting junk files

vu.dircheck(IMGDIRNAME)
os.system(f"xcopy /s /y /q simple_images {IMGDIRNAME}")
os.system(f"rmdir /s /q simple_images")

vu.msg("Job is done!")

input("Press any key to exit...")
