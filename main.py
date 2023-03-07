# Requirements:
# 1. pytube, just run "pip install pytube" in terminal
# 2. ffmpeg, download archive from official website
#    then find ffmpeg.exe, move it to directory of your choice
#    then run "set PATH=%PATH%;C:/your/dir/here" in terminal

import os
import time

from urllib.error import URLError
from pytube import YouTube

DIRNAME = "ytfootage"
FORBIDDEN_CHARS = "|:<>/?*\\\""


def msg(message: str) -> None:
	print(message)
	time.sleep(0.5)


def clear_name(text: str, chars=FORBIDDEN_CHARS) -> str:
	for char in chars:
		if char in text:
			text = text.replace(char, "")
	return text


def restart() -> None:
	input("Press any key to restart...")
	os.system(f"cls && {os.path.basename(__file__)}")


user_input = input("Enter link or list of links divided by whitespace: ")

links = [i for i in user_input.split() if "youtu" in i]
if not links:
	msg("Links are invalid. Please try again...")
	restart()

os.system(f"if not exist {DIRNAME} mkdir {DIRNAME}")

for idx, link in enumerate(links, 1):
	msg(f"Trying to download video {idx} of {len(links)}...")

	flag = False
	while not flag:
		try:
			yt_streams = YouTube(link).streams
			flag = True
		except URLError:
			msg("Internet connection problems...")
			msg("Trying again in 5 seconds...")
			time.sleep(5)

	vurl = yt_streams.filter(adaptive=True).order_by("resolution")[-1].url
	aurl = yt_streams.get_by_tag(18).url
	sett = "-acodec aac -b:a 192k -avoid_negative_ts make_zero"
	maps = "-map 0:v:0 -map 1:a:0"
	path = f"./{DIRNAME}/{clear_name(yt_streams[0].title)}.mp4"
	os.system(f'ffmpeg -i "{vurl}" -i "{aurl}" {sett} {maps} "{path}"')

	msg(f"Video {idx} of {len(links)} is done!")

msg("Job is done!")
input("Press any key to exit...")
