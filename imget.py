import os

from PIL import Image, UnidentifiedImageError
import simple_image_download.simple_image_download as idl
import vesputils as vu
from imgconv import prepare_images
from settings import IMGDIRNAME, IMGDEFCOUNT

user_req = input("Enter your requests divided by comma: ").replace(" ", "+").replace(",+", " ")

try:
    count = int(input("How many images do you need?: "))
    count = count if count > 0 else IMGDEFCOUNT
except ValueError:
    count = IMGDEFCOUNT

vu.msg(f"Trying to download {count} images for each request...")

my_downloader = idl.Downloader()
my_downloader.download(user_req, limit=count)  

'''
TODO: Make a proper http.client.IncompleteRead 
      and requests.excpetions.ConnectionError handling
'''

prepare_images()  # Converting images and deleting junk files

os.system(f"if not exist {IMGDIRNAME} mkdir {IMGDIRNAME}")
os.system(f"xcopy /s /y /q simple_images {IMGDIRNAME}")
os.system(f"rmdir /s /q simple_images")

vu.msg("Job is done!")

input("Press any key to exit...")
