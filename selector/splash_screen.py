# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""splash_screen.py: When the program is run, will be the screen that they see first."""
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory # will need later on
from selection import directory, video

root = Tk()
root.geometry('500x500')
root.iconbitmap('../img/fletcher-family-crest.jpg.ico')
root.title('Fletcher Video Encoder')


# returns directory selected from file dialog
def directory_button_command():
    path_to_directory = askdirectory()
    chosen_directory = directory.Directory(path_to_directory)
    return chosen_directory


# returns video selected from file dialog
def video_button_command():
    path_to_video = askopenfilename()
    chosen_video = video.Video(path_to_video)
    return chosen_video


directory_button = Button(root, text='Directory', command=directory_button_command)
directory_button.pack(side=LEFT, expand=YES)

video_button = Button(root, text='Video', command=video_button_command)
video_button.pack(side=RIGHT, expand=YES)

root.mainloop()