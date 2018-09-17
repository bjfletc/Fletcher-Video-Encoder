# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""splash_screen.py: When the program is run, will be the screen that they see first."""
import sys
import os
import threading
path_to_append = os.getcwd()
path_to_append = path_to_append[0:path_to_append.rfind('\\')]
sys.path.append(path_to_append)
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory # will need later on
from selection import directory, video
from encoder import ffmpeg_command
import fletcher_encoder
import ffmpeg_downloader
# TODO: learn how to create a SplashScreen OOP class
fletcher_video_encoder = fletcher_encoder.Encoder()

# TODO: create module for each command... open in Users default Videos...
def directory_button_command():
    path_to_directory = askdirectory(initialdir='C:\\Users\\')
    chosen_directory = directory.Directory(path_to_directory)
    print(path_to_directory)
    name_of_file_or_directory_label.config(text='Encoding: ' + chosen_directory.videos()[0])
    return chosen_directory


def video_button_command():
    path_to_video = askopenfilename(initialdir='C:\\Users\\', filetypes = (('MP4', '*.mp4'),
                                    ('AVI', '*.avi'), ('MKV', '*.mkv')))
    chosen_video = video.Video(path_to_video)
    print(path_to_video)
    print(chosen_video.title())
    name_of_file_or_directory_label.config(text='Encoding: ' + chosen_video.complete_path())
    # ffmpeg_encoder.start_thread(ffmpeg_command.ffmpeg_cmd(chosen_video)) # runs ffmpeg in a thread
    fletcher_video_encoder.start_subprocess_thread(ffmpeg_command.ffmpeg_cmd(chosen_video))
    return chosen_video


root = Tk()
root.geometry('500x500')
root.iconbitmap('../img/fletcher-family-crest.jpg.ico')
root.title('Fletcher Video Encoder -- Installing FFMPEG...')


# adding for TEST0
def do_something():
    # check if saving
    # if not:
    fletcher_video_encoder.stop_subprocess_thread()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', do_something)  # root is your root window

# add GUI components
# COMPLETED Create Separate Class for GUI

label_frame = Frame(root)
label_frame.pack(side=TOP, fill=X)

name_of_file_or_directory_label = Label(label_frame)
name_of_file_or_directory_label.pack()

buttons_frame = Frame(root)
buttons_frame.pack(side=BOTTOM, fill=X, ipady=25)

directory_button_frame = Frame(buttons_frame, bg='green')
directory_button_frame.pack(side=LEFT, fill=Y, ipadx=100)

directory_button = Button(directory_button_frame, text='Directory', command=directory_button_command)
directory_button.pack(anchor='center', expand=YES)

video_button_frame = Frame(buttons_frame, bg='yellow')
video_button_frame.pack(side=RIGHT, fill=Y, ipadx=125)

video_button = Button(video_button_frame, text='Video', command=video_button_command)
video_button.pack(anchor='center', expand=YES)

# sloppy code... refactor later...
current_directory = os.getcwd()
os.chdir('..')
program_root_directory = os.getcwd()
print(program_root_directory)


if os.path.isdir('ffmpeg') == False:
    download_thread = threading.Thread(target=ffmpeg_downloader.download_ffmpeg())
    download_thread.daemon = True
    name_of_file_or_directory_label.config(text='Please wait while I install ffmpeg...')
    download_thread.start()
    name_of_file_or_directory_label.config(text='Finished... you may choose a Video now...')

root.title('Fletcher Video Encoder')

os.chdir(current_directory)

root.mainloop()