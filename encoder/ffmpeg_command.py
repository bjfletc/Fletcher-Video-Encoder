# Author: Brandon J. Fletcher
# Created  : Tuesday, Sep 04, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""command.py: will return the string version of the ffmpeg command."""
from selection.video import Video
import sys
import os
sys.path.append('..\\ffmpeg\\bin')

username = os.getlogin()
video_dir = 'C:\\Users\\' + username + '\\Videos\\'
print(video_dir)
# TODO: Change from Static Output Location...
OUTPUT = video_dir


def ffmpeg_cmd(video=Video('')):
    path_to_video_to_encode = video.complete_path()
    video_to_encode = video.title()
    print('Video = ' + video_to_encode)
    index_of_format = video_to_encode.rfind('.')
    cmd = 'ffmpeg -i ' + '"' + path_to_video_to_encode + '"' + \
          ' -c:v libx264 -vf scale=1280:720 -r 30 -c:a copy ' + '"' \
          + OUTPUT + video_to_encode[:index_of_format] + '.mp4' + '"'
    print(cmd)
    return cmd


if __name__ == '__main__':
    print('Nothing to See Here...')
