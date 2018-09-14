# Author: Brandon J. Fletcher
# Created  : Thursday, Sep 13, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""main_console.py: will house the launch screen of the application. """

from gui import btn_cmds    # needed for the main consoles dir/vid buttons
from tkinter import *


# creating a class definition of what the main console should display as
class MainConsole:

    root = Tk()     # main window of the application
    root.geometry('500x500')
    root.iconbitmap('../img/fletcher-family-crest.jpg.ico')     # Fletcher Family Crest for Window
    root.title('Fletcher Video Encoder')

    name_of_video_being_encoded_frame = Frame(root)         # frame to house the name of what is being encoded
    name_of_video_being_encoded_frame.pack(side=TOP, fill=X)

    name_of_video_being_encoded_label = Label(name_of_video_being_encoded_frame)  # displays what is being encoded
    name_of_video_being_encoded_label.pack()

    buttons_frame = Frame(root)
    buttons_frame.pack(side=BOTTOM, fill=X, ipady=25)

    # [Directory]
    directory_button_frame = Frame(buttons_frame, bg='green')
    directory_button_frame.pack(side=LEFT, fill=Y, ipadx=100)

    # TODO: whenever btn is pressed change label for what is being encoded...
    directory_button = Button(directory_button_frame, text='Directory', command=btn_cmds.dir_btn_cmd)
    directory_button.pack(anchor='center', expand=YES)

    # [Video]
    video_button_frame = Frame(buttons_frame, bg='yellow')
    video_button_frame.pack(side=RIGHT, fill=Y, ipadx=125)

    # TODO: whenever btn is pressed change label for what is being encoded...
    video_button = Button(video_button_frame, text='Video', command=btn_cmds.vid_btn_cmd)
    video_button.pack(anchor='center', expand=YES)

    def start(self):
        return self.root.mainloop()

    # TODO: method to check validity of local version of ffmpeg...
    """
    def verify_ffmpeg_installation(self):
        if True:
            # return true and continue with program...
        elif False:
            # install ffmpeg... then continue with program...
    """

    # TODO: create method that terminates thread
    """
    def exit(self):
        # terminate thread...
        return ...
    """

    # used to change the label to the name of whatever is being encoded currently
    def set_contents_of_video_being_encoded_label(self, string_name_of_video_or_directory):
        return self.name_of_video_being_encoded_label.config(text=string_name_of_video_or_directory)


if __name__ == '__main__':
    test_flight = MainConsole().start()
    test_flight.set_contents_of_video_being_encoded_label("Magic...")