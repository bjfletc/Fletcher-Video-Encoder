# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""encoder.py: will be the main method for encoding."""
import subprocess
from selection.video import Video
# COMPLETE(1): learn how to pipe the process of encoding from cmd
# TODO(2): if elif logic for if it is a directory or a video being encoded
# TODO(3): create method for output file location

OUTPUT = 'C:\\Users\\Brandon\\Videos\\'
print(OUTPUT)


def ffmpeg_video_cmd(video_path=Video('')):
    path_to_video_to_encode = video_path.complete_path()
    video_to_encode = video_path.title()
    print(video_to_encode)
    index_of_format = video_to_encode.rfind('.')
    ffmpeg_cmd = 'ffmpeg -i ' + '"' + path_to_video_to_encode + '"' + \
                 ' -c:v libx264 -vf scale=1280:720 -r 30 -c:a copy ' + '"' \
                 + OUTPUT + video_to_encode[:index_of_format] + '.mp4' + '"'
    print(ffmpeg_cmd)
    return ffmpeg_cmd


def start_subprocess(command):
    cmd = command
    ffmpeg_pipe = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, shell=True,
                                   universal_newlines=True)

    ferr = ffmpeg_pipe.stderr
    for line in ferr:
        print(line)

    ferr.close()
    ffmpeg_pipe.wait()
    if ffmpeg_pipe.returncode != 0:
        raise subprocess.CalledProcessError(ffmpeg_pipe.returncode, cmd)


if __name__ == '__main__':
    path = 'W:\\Brandon J. Fletcher\\Computer Programming\\Code\\Python\\Python Playground\\S01E02.mkv'
    test_video_0 = Video(path)
    print(ffmpeg_video_cmd(test_video_0))
    start_subprocess(ffmpeg_video_cmd(test_video_0))