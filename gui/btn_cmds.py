# Author: Brandon J. Fletcher
# Created  : Tuesday, Sep 11, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""btn_cmds.py: module that holds the response for the event-listeners in the
    buttons of the GUI."""

from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from selection import directory, video
from encoder import ffmpeg_command
import fletcher_encoder

# TODO: figure out a way to change the label of the splash screen...
encoding_engine = fletcher_encoder.Encoder()


def dir_btn_cmd():
    path_to_directory = askdirectory(initialdir='C:\\Users\\')
    chosen_directory = directory.Directory(path_to_directory)
    Label(text=chosen_directory.name()).pack()
    # TODO: add for in threading logic to encode all vids in a dir
    return chosen_directory


def vid_btn_cmd():
    path_to_video = askopenfilename(initialdir='C:\\Users\\', filetypes=(('MP4', '*.mp4'),
                                    ('AVI', '*.avi'), ('MKV', '*.mkv')))
    chosen_video = video.Video(path_to_video)
    Label(text=chosen_video.title()).pack()
    encoding_engine.start_subprocess_thread(ffmpeg_command.ffmpeg_cmd(chosen_video))
    return chosen_video


if __name__ == '__main__':
    print('Do Nothing...')
