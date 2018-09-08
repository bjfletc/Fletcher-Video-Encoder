# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""ffmpeg_encoder.py: will be the main method for encoding."""
import threading
from encoder import ffmpeg_subprocess
from encoder import ffmpeg_command
from selection.video import Video
import ctypes # added for test0
# COMPLETE(1): learn how to pipe the process of encoding from cmd
# TODO(2): if elif logic for if it is a directory or a video being encoded # Not Sure Needed...
# TODO(3): create method for output file location
# TODO(1): need a way to stop the thread when the Windows is closed.

#ffmpeg_pipe = ffmpeg_subprocess.ffmpeg_pipe


def start_thread(encoding):
    t = threading.Thread(target=ffmpeg_subprocess.start_subprocess, args=(encoding,))
    t.start()
    return t


def stop_thread():
    #ffmpeg_pipe = thread
    ''' Removed for Test0
    thread.threading.Event().set()
    threading.Thread.join(thread, timeout=None)
    return print('Need a way to stop my thread...')
    '''
    ctypes.windll.kernel32.TerminateProcess(int(ffmpeg_pipe._handle), -1)
    return print('Subprocess Terminated...')


if __name__ == '__main__':
    path = 'W:\\Brandon J. Fletcher\\Computer Programming\\Code\\Python\\Python Playground\\S01E02.mkv'
    test_video_0 = Video(path)
    print(ffmpeg_command.ffmpeg_cmd(test_video_0))
    # start_subprocess(ffmpeg_video_cmd(test_video_0))
    running_thread = start_thread(ffmpeg_command.ffmpeg_cmd(test_video_0))
