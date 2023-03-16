"""
DIRECTORY NAMES AND OTHER SETTINGS
"""

# ytget
DIRNAME: str = "ytfootage"
FFMPEGARGS: str = "-acodec aac -b:a 192k -avoid_negative_ts make_zero -map 0:v:0 -map 1:a:0"

# imget
IMGDIRNAME: str = "pictures"
IMGDEFCOUNT: int = 10
IMGJUNKSIZE: tuple = (80, 36)

# getreqs
FFMPEGURL: str = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
GIDDIR: str = "C:\\Users\\*\\AppData\\Local\\Programs\\Python\\*\\Lib\\site-packages\\google_images_download"
GIDFIXURL: str = "https://github.com/Joeclinton1/google-images-download/" \
                 "raw/patch-1/google_images_download/google_images_download.py"

# version
VERSION: str = "0.1.1, Chitin"
