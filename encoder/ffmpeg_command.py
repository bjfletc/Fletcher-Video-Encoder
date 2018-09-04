# Author: Brandon J. Fletcher
# Created  : Tuesday, Sep 04, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""command.py: will return the string version of the ffmpeg command."""

OUTPUT = 'C:\\Users\\Brandon\\Videos\\'


def ffmpeg_cmd(video):
    path_to_video_to_encode = video.complete_path()
    video_to_encode = video.title()
    print('Video = ' + video_to_encode)
    index_of_format = video_to_encode.rfind('.')
    cmd = 'ffmpeg -i ' + '"' + path_to_video_to_encode + '"' + \
          ' -c:v libx264 -vf scale=1280:720 -r 30 -c:a copy ' + '"' \
          + OUTPUT + video_to_encode[:index_of_format] + '.mp4' + '"'
    print(cmd)
    return cmd
