# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""ffmpeg_encoder.py: will be the main method for encoding."""
import threading
from encoder import ffmpeg_subprocess
from encoder import ffmpeg_command
from selection.video import Video
# COMPLETE(1): learn how to pipe the process of encoding from cmd
# TODO(2): if elif logic for if it is a directory or a video being encoded # Not Sure Needed...
# TODO(3): create method for output file location
# TODO(1): need a way to stop the thread when the Windows is closed.


def start_thread(encoding):
    t = threading.Thread(target=ffmpeg_subprocess.start_subprocess, args=(encoding,))
    t.start()
    return t


def stop_thread(thread):
    thread.threading.Event().set()
    threading.Thread.join(thread, timeout=None)
    return print('Need a way to stop my thread...')


if __name__ == '__main__':
    path = 'W:\\Brandon J. Fletcher\\Computer Programming\\Code\\Python\\Python Playground\\S01E02.mkv'
    test_video_0 = Video(path)
    print(ffmpeg_command.ffmpeg_cmd(test_video_0))
    # start_subprocess(ffmpeg_video_cmd(test_video_0))
    running_thread = start_thread(ffmpeg_command.ffmpeg_cmd(test_video_0))
