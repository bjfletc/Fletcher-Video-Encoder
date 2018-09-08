# Author: Brandon J. Fletcher
# Created  : Friday, Sep 07, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""fletcher_encoder.py is going to be the main module for encoding videos."""

import threading
import subprocess
import sys
import ctypes
sys.path.append('W:\Brandon J. Fletcher\Computer Programming\Code\Python\Fletcher Video Encoder')


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


    def stop_subprocess_thread(self):
        self.ffmpeg_pipe.terminate()
        #ctypes.windll.kernel32.TerminateProcess(int(self.ffmpeg_pipe._handle), -1)
        return print('Subprocess Terminated...')


if __name__ == '__main__':
    print('')
