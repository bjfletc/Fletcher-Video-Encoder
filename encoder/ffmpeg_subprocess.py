# Author: Brandon J. Fletcher
# Created  : Tuesday, Sep 04, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""ffmpeg_subprocess.py: will start the ffmpeg command."""


import subprocess


def start_subprocess(command):
    cmd = command
    # test multiprocessing.fork()
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
    print('Nothing to See Here...')
