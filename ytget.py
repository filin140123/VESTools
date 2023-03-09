import os
import time

from urllib.error import URLError
from pytube import YouTube

from settings import DIRNAME
from scenecutter import cut_videos
import vesputils as vu


def restart() -> None:
    input("Press any key to restart...")
    os.system(f"cls && {os.path.basename(__file__)}")


user_input = input("Enter link or list of links divided by whitespace: ")

links = [i for i in user_input.split() if "youtu" in i]
if not links:
    vu.msg("Links are invalid. Please try again...")
    restart()

os.system(f"if not exist {DIRNAME} mkdir {DIRNAME}")

for idx, link in enumerate(links, 1):
    vu.msg(f"Trying to download video {idx} of {len(links)}...")

    flag = False
    while not flag:
        try:
            yt_streams = YouTube(link).streams
            flag = True
        except URLError:
            vu.msg("Internet connection problems...")
            vu.msg("Trying again in 5 seconds...")
            time.sleep(5)

    vurl = yt_streams.filter(adaptive=True).order_by("resolution")[-1].url
    aurl = yt_streams.get_by_itag(18).url
    sett = "-acodec aac -b:a 192k -avoid_negative_ts make_zero"
    maps = "-map 0:v:0 -map 1:a:0"
    path = f"./{DIRNAME}/{vu.clear_name(yt_streams[0].title)}.mp4"
    os.system(f'ffmpeg -i "{vurl}" -i "{aurl}" {sett} {maps} "{path}"')

    vu.msg(f"Video {idx} of {len(links)} is done!")

vu.msg("All downloads is done!")
action = input("Do you want to cut videos by scenes? (y/n): ")
if action in "yY":
    cut_videos()

vu.msg("Job is done!")
input("Press any key to exit...")
