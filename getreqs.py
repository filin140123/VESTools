"""
Requirements autoinstall
"""

import os
import glob
import shutil
from zipfile import ZipFile

import vesputils as vu
from settings import FFMPEGURL, GIDDIR, GIDFIXURL

try:
    import wget
except ImportError:
    os.system("pip install wget")
    import wget

# Installing python packages
vu.msg("Installing python packages...")
os.system("pip install -r requirements.txt")

# Fixing google_image_download
vu.msg("Fixing google_images_download...")
gid_dir = glob.glob(GIDDIR)[0]
os.remove(f"{gid_dir}\\google_images_download.py")
wget.download(GIDFIXURL, out=gid_dir)
with open(f"{gid_dir}\\google_images_download.py", "r", encoding="utf-8") as f:
    data = f.readlines()
with open(f"{gid_dir}\\google_images_download.py", "w", encoding="utf-8") as f:
    for idx, line in enumerate(data, 1):
        if idx == 407:
            f.writelines(" " * 12 + "info = data[23]" + "\n")
        else:
            f.writelines(line)

# # Downloading FFMPEG
vu.msg("Downloading FFMPEG...")
wget.download(FFMPEGURL)

# Extracting ffmpeg.exe
vu.msg("Extracting ffmpeg.exe...")
with ZipFile("ffmpeg-release-essentials.zip") as archive:
    filenames = archive.namelist()
    for name in filenames:
        if name.endswith("ffmpeg.exe"):
            exe_path = name
            archive.extract(name, ".")

# Removing temporary files
vu.msg("Removing temporary files...")
os.system(f"move {os.path.abspath(exe_path)} {os.path.abspath('.')}")
os.remove("ffmpeg-release-essentials.zip")
shutil.rmtree(*[i for i in os.listdir(".") if i.endswith("build")])

# # Installation complete
vu.msg("Installation complete!")
input("Press any key to exit...")
