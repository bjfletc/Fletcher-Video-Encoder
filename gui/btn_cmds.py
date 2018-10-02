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
import sys
sys.path.append('../')


encoding_engine = fletcher_encoder.Encoder()


def dir_btn_cmd():
    path_to_directory = askdirectory(initialdir='C:\\Users\\')
    chosen_directory = directory.Directory(path_to_directory)
    list_of_videos_in_directory = chosen_directory.videos()
    Label(text="Encoding: " + chosen_directory.name()).pack()
    # TODO: make dir function wait until previous video is completed encoding to start the next
    for current_video in list_of_videos_in_directory:
        print(current_video.complete_path())
        print(str(current_video))
        encoding_engine.start_subprocess_thread(ffmpeg_command.ffmpeg_cmd(current_video))

    return chosen_directory


def vid_btn_cmd():
    path_to_video = askopenfilename(initialdir='C:\\Users\\', filetypes=(('MP4', '*.mp4'),
                                    ('AVI', '*.avi'), ('MKV', '*.mkv')))
    chosen_video = video.Video(path_to_video)
    Label(text=chosen_video.title()).pack()
    encoding_engine.start_subprocess_thread(ffmpeg_command.ffmpeg_cmd(chosen_video))
    return chosen_video


def stop_whatever_you_are_doing():
    encoding_engine.stop_subprocess_thread()
    return exit()


if __name__ == '__main__':
    print('Do Nothing...')
