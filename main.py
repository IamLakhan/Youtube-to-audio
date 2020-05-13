import os
from pytube import YouTube
import ffmpeg

link = input('Enter youtube link: ')
yt = YouTube(link)
title = yt.title
question = input(f"Is '{title}'' the title of the video?(y/n): ")
if question.lower() == 'y':
	stream = yt.streams.filter(only_audio = True).first()
	print('Downloading from YouTube...')
	stream.download()
	print('Downloaded!')
	cmd = f'mv "{title}.mp4" input.mp4'
	os.system(cmd)
	print('Converting to mp3...')
	cmd = f'ffmpeg -i input.mp4 audio.mp3 >/dev/null 2>&1'
	os.system(cmd)
	cmd = f'rm -rf input.mp4'
	os.system(cmd)
	cmd = f'mv audio.mp3 "{title}.mp3"'
	os.system(cmd)
	print('Done!')
else: print('try again')