# Author: Brandon J. Fletcher
# Created  : Friday, Sep 07, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""fletcher_encoder.py is going to be the main module for encoding videos."""

import threading
import subprocess
import sys
import os
dir_to_append = os.getcwd()
sys.path.append(dir_to_append)
sys.path.append('\\ffmpeg\\bin')
print(dir_to_append[0:dir_to_append.rfind('\\')] + '\\ffmpeg\\bin\\')
os.environ['PATH'] += os.pathsep + ((dir_to_append[0:dir_to_append.rfind('\\')]) + '\\ffmpeg\\bin\\')


class Encoder:

    def __init__(self):
        self.ffmpeg_pipe = subprocess

    def start_subprocess(self, command):
        cmd = command
        # test multiprocessing.fork()
        # global ffmpeg_pipe  #added for test0
        self.ffmpeg_pipe = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            universal_newlines=True)

        ferr = self.ffmpeg_pipe.stderr
        for line in ferr:
            print(line)

        ferr.close()
        self.ffmpeg_pipe.wait()
        if self.ffmpeg_pipe.returncode != 0:
            raise subprocess.CalledProcessError(self.ffmpeg_pipe.returncode, cmd)

    def start_subprocess_thread(self, going_to_encode):
        t = threading.Thread(target=self.start_subprocess, args=(going_to_encode,))
        t.daemon = True
        t.start()
        return t

    # TODO: learn leaner way to stop subprocess/thread maybe its own class?
    def stop_subprocess_thread(self):
        # warning because it says it cannot find, but is a member of subprocess.Popen...
        self.ffmpeg_pipe.terminate()
        return print('Subprocess Terminated...')


if __name__ == '__main__':
    print('')
