"""
Getting YT videos
"""

import os

from urllib.error import URLError
from pytube import YouTube

import vesputils as vu
from settings import DIRNAME, FFMPEGARGS
from scenecutter import cut_videos


links = None
while True:  # Is the user input YT links?
    user_input = input("Enter link or list of links divided by whitespace: ")
    links = [i for i in user_input.split() if "youtu" in i]

    if not links:
        vu.msg("Links are invalid. Please try again...")
    else:
        break

os.system(f"if not exist {DIRNAME} mkdir {DIRNAME}")

videos = []

for idx, link in enumerate(links, 1):
    vu.msg(f"Trying to download video {idx} of {len(links)}...")

    yt_streams = None
    for i in range(1, 11):
        try:
            yt_streams = YouTube(link).streams
        except URLError:
            vu.msg("Internet connection problems...")
            vu.msg("Trying again in 5 seconds...")
            vu.countdown(5)
        else:
            break
    else:
        vu.msg("Download failed 10 times. Exiting...")
        quit()

    vurl = yt_streams.filter(adaptive=True).order_by("resolution")[-1].url
    aurl = yt_streams.get_by_itag(18).url
    name = vu.clear_name(yt_streams[0].title)
    path = f"./{DIRNAME}/{name}.mp4"
    os.system(f'ffmpeg -i "{vurl}" -i "{aurl}" {FFMPEGARGS} "{path}"')

    videos.append(path)
    vu.msg(f"Video {idx} of {len(links)} is done!")

vu.msg("All downloads is done!")

action = input("Do you want to cut videos by scenes? (y/n): ")
if action in ("y", "Y", "yes", "Yes", "YES"):
    cut_videos(videos)

vu.msg("Job is done!")
input("Press any key to exit...")
