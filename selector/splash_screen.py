# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""splash_screen.py: When the program is run, will be the screen that they see first."""

import os
import threading
from tkinter import *
from gui import btn_cmds
import ffmpeg_downloader
import fletcher_encoder
import sys
path_to_append = os.getcwd()
path_to_append = path_to_append[0:path_to_append.rfind('\\')]
sys.path.append(path_to_append)


fletcher_video_encoder = fletcher_encoder.Encoder()

# main windows that the program resides in
root = Tk()
root.geometry('500x500')
root.iconbitmap('../img/fletcher-family-crest.jpg.ico')
root.title('Fletcher Video Encoder -- Installing FFMPEG...')


def do_something():
    # check if saving
    # if not:
    fletcher_video_encoder.stop_subprocess_thread()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', do_something)  # root is your root window


# TODO Create Separate Class for GUI

label_frame = Frame(root)
label_frame.pack(side=TOP, fill=X)

name_of_file_or_directory_label = Label(label_frame)
name_of_file_or_directory_label.pack()

buttons_frame = Frame(root)
buttons_frame.pack(side=BOTTOM, fill=X, ipady=25)

directory_button_frame = Frame(buttons_frame, bg='green')
directory_button_frame.pack(side=LEFT, fill=Y, ipadx=100)

directory_button = Button(directory_button_frame, text='Directory', command=btn_cmds.dir_btn_cmd)
directory_button.pack(anchor='center', expand=YES)

video_button_frame = Frame(buttons_frame, bg='yellow')
video_button_frame.pack(side=RIGHT, fill=Y, ipadx=125)

video_button = Button(video_button_frame, text='Video', command=btn_cmds.vid_btn_cmd)
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

if __name__ == '__main__':
    print('Do nothing...')