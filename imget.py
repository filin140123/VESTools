import os

from PIL import Image, UnidentifiedImageError
import simple_image_download.simple_image_download as idl
import vesputils as vu
from imgconv import prepare_images
from settings import IMGDIRNAME, IMGDEFCOUNT

user_req = input("Enter your requests divided by comma: ")
user_cnt = int(input("How many images do you need?: "))

count = vu.posdef(user_cnt, IMGDEFCOUNT)
clreq = user_req.replace(" ", "+").replace(",+", " ")

vu.msg(f"Trying to download {count} images for each request...")

my_downloader = idl.Downloader()
my_downloader.download(clreq, limit=count)  

'''
TODO: Make a proper http.client.IncompleteRead 
      and requests.excpetions.ConnectionError handling
'''

prepare_images()  # Converting images and deleting junk files

vu.dircheck(IMGDIRNAME)
os.system(f"xcopy /s /y /q simple_images {IMGDIRNAME}")
os.system(f"rmdir /s /q simple_images")

vu.msg("Job is done!")

input("Press any key to exit...")
