# Author: Brandon J. Fletcher
# Created  : Thursday, Sep 13, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""main_console.py: will house the launch screen of the application. """

from gui import btn_cmds    # needed for the main consoles dir/vid buttons
from tkinter import *
import os
import threading
import ffmpeg_downloader


# creating a class definition of what the main console should display as
class MainConsole:

    root = Tk()     # main window of the application
    root.geometry('500x500')
    root.iconbitmap('../img/fletcher-family-crest.jpg.ico')     # Fletcher Family Crest for Window
    root.title('Fletcher Video Encoder')

    buttons_frame = Frame(root)
    buttons_frame.pack(side=BOTTOM, fill=X, ipady=25)

    # [Directory]
    directory_button_frame = Frame(buttons_frame, bg='green')
    directory_button_frame.pack(side=LEFT, fill=Y, ipadx=100)

    # COMPLETED: whenever btn is pressed change label for what is being encoded...
    directory_button = Button(directory_button_frame, text='Directory', command=btn_cmds.dir_btn_cmd)
    directory_button.pack(anchor='center', expand=YES)

    # [Video]
    video_button_frame = Frame(buttons_frame, bg='yellow')
    video_button_frame.pack(side=RIGHT, fill=Y, ipadx=125)

    # COMPLETED: whenever btn is pressed change label for what is being encoded...
    video_button = Button(video_button_frame, text='Video', command=btn_cmds.vid_btn_cmd)
    video_button.pack(anchor='center', expand=YES)

    def start(self):
        # verify ffmpeg installation...
        # TODO (#1): verify thread functions properly in this module...
        self.verify_ffmpeg_installation()
        return self.root.mainloop()

    # TODO: method to check validity of local version of ffmpeg...
    def verify_ffmpeg_installation(self):

        cwd = os.getcwd()
        os.chdir('..')

        if os.path.isdir('ffmpeg'):
            print('ffmpeg already successfully installed on system.')

        else:
            download_thread = threading.Thread(target=ffmpeg_downloader.download_ffmpeg())
            download_thread.daemon = True
            self.root.title('Fletcher Video Encoder -- Installing FFMPEG')
            tmp_label = Label(text='Please wait while I install ffmpeg...').pack()
            download_thread.start()
            tmp_label.config(text='Finished... you may choose a Video now...')

        os.chdir(cwd)
        return self.root.title('Fletcher Video Encoder -- FFMPEG Successfully Installed')

    # TODO: create method that terminates thread
    """
    def exit(self):
        # terminate thread...
        return ...
    """


if __name__ == '__main__':
    test_flight = MainConsole().start()
    test_flight.set_contents_of_video_being_encoded_label("Magic...")
