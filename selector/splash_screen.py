# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""splash_screen.py: When the program is run, will be the screen that they see first."""
import sys
import os
path_to_append = os.getcwd()
path_to_append = path_to_append[0:path_to_append.rfind('\\')]
sys.path.append(path_to_append)
print(path_to_append)
#sys.path.append('W:\Brandon J. Fletcher\Computer Programming\Code\Python\Fletcher Video Encoder')
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory # will need later on
from selection import directory, video
from encoder import ffmpeg_command
import fletcher_encoder
# TODO(4): learn how to create a SplashScreen OOP class
fletcher_video_encoder = fletcher_encoder.Encoder()

# COMPLETED(6): if button is pressed, open a new window for encoding that has the folder name
# returns directory selected from file dialog


def directory_button_command():
    path_to_directory = askdirectory(initialdir='W:\Brandon J. Fletcher\Videos')
    chosen_directory = directory.Directory(path_to_directory)
    print(path_to_directory)
    name_of_file_or_directory_label.config(text='Encoding: ' + chosen_directory.videos()[0])
    return chosen_directory


# COMPLETED(7): if button is pressed, open a new window for encoding that has the video name
# returns video selected from file dialog
def video_button_command():
    path_to_video = askopenfilename(initialdir='W:\Brandon J. Fletcher\Videos', filetypes = (('MP4', '*.mp4'),
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
root.title('Fletcher Video Encoder')


# adding for TEST0
def doSomething():
    # check if saving
    # if not:
    fletcher_video_encoder.stop_subprocess_thread()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window

# add GUI components

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


root.mainloop()