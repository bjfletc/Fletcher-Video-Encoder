# Author: Brandon J. Fletcher
# Created  : Thursday, Sep 13, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""main_console.py: will house the launch screen of the application. """

from gui import btn_cmds    # needed for the main consoles dir/vid buttons
from tkinter import *

root = Tk()     # main window of the application
root.geometry('500x500')
root.iconbitmap('../img/fletcher-family-crest.jpg.ico')     # Fletcher Family Crest for Window
root.title('Fletcher Video Encoder')

name_of_video_being_encoded_frame = Frame(root)         # frame to house the name of what is being encoded
name_of_video_being_encoded_frame.pack(side=TOP, fill=X)

name_of_video_being_encoded_label = Label(name_of_video_being_encoded_frame)  # actually displays what is being encoded
name_of_video_being_encoded_label.pack()

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

root.mainloop()

'''
if __name__ == '__main__':
    btn_cmds.vid_btn_cmd()
'''
