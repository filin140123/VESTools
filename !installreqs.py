import os
import shutil
from zipfile import ZipFile

import vesputils as vu

# Installing python packages
vu.msg("Installing python packages...")
os.system("pip install requests wget click-shell pillow pytube scenedetect imagesize")

import wget

# Downloading FFMPEG
vu.msg("Downloading FFMPEG...")
wget.download("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")

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

# Installation complete
vu.msg("Installation complete!")
input("Press any key to exit...")
