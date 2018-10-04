# Author: Brandon J. Fletcher
# Created  : Thursday, Sep 13, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""main_console.py: will house the launch screen of the application. """

# TODO: find way to avoid putting this at the top of each module...
import sys
sys.path.append('../')
from gui import btn_cmds    # needed for the main consoles dir/vid buttons
from tkinter import *
import time
import os
import threading
import ffmpeg_downloader


# creating a class definition of what the main console should display as
class MainConsole:

    root = Tk()     # main window of the application
    root.geometry('900x400')
    root.iconbitmap('../img/fletcher-family-crest.jpg.ico')     # Fletcher Family Crest for Window
    root.configure(background="#535760")
    root.title('Fletcher Video Encoder')

    # COMPLETED: Create Method that Closes Program and Stops Thread...
    # need check here to see if something is being encoded and if this protocol is needed or not.
    if threading.active_count() >= 1:
        root.protocol('WM_DELETE_WINDOW', btn_cmds.stop_whatever_you_are_doing)

    buttons_frame = Frame(root)
    buttons_frame.pack(side=BOTTOM, fill=X, ipady=25)

    # [Directory]
    directory_button_frame = Frame(buttons_frame, bg='green')
    directory_button_frame.pack(side=LEFT, fill=Y, ipadx=100)

    directory_button = Button(directory_button_frame, text='Directory', command=btn_cmds.dir_btn_cmd)
    directory_button.pack(anchor='center', expand=YES)

    # [Video]
    video_button_frame = Frame(buttons_frame, bg='yellow')
    video_button_frame.pack(side=RIGHT, fill=Y, ipadx=125)

    video_button = Button(video_button_frame, text='Video', command=btn_cmds.vid_btn_cmd)
    video_button.pack(anchor='center', expand=YES)

    # COMPLETED: discover way to change title & label depending on if ffmpeg is installed or not
    def check_download(self):

        tmp_label = Label(self.root)
        tmp_label.pack()
        print(os.getcwd())
        print(str(os.path.isdir('ffmpeg')))
        while not os.path.isdir('ffmpeg'):
            self.root.title('Fletcher Video Encoder -- Installing FFMPEG')
            tmp_label.config(text='Installing FFMPEG... Please wait...')
            tmp_label.config(background="#535760")

        self.root.title('Fletcher Video Encoder -- FFMPEG Successfully Installed')
        tmp_label.config(text='FFMPEG Successfully Installed.')
        tmp_label.config(background="#535760")
        time.sleep(5)
        self.root.title('Fletcher Video Encoder')
        tmp_label.config(text='Continue by Selecting a Video...')
        time.sleep(5)
        tmp_label.destroy()

    def start(self):
        # verify ffmpeg installation...
        self.install_ffmpeg()
        check_download_thread = threading.Thread(name='ffmpeg_download', target=self.check_download)
        check_download_thread.daemon = True
        check_download_thread.start()
        return self.root.mainloop()

    def install_ffmpeg(self):

        os.chdir('../')     # change so ffmpeg installs in the root dir

        if os.path.isdir('ffmpeg'):
            self.root.title('Fletcher Video Encoder -- FFMPEG Successfully Installed')
        else:
            download_thread = threading.Thread(name='Installer', target=ffmpeg_downloader.download_ffmpeg)
            download_thread.daemon = True
            download_thread.start()
        print(str(threading.active_count()))
        return print('...Installing...')


if __name__ == '__main__':
    test_flight = MainConsole().start()
