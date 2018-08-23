# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""splash_screen.py: When the program is run, will be the screen that they see first."""
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory # will need later on
from selection import directory, video

class SplashScreen(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()

    def make_widgets(self):
        directory_button = Button(self, text='Directory', command=self.directory_button_command)
        directory_button.pack(side=LEFT)

        video_button = Button(self, text='Video', command=self.video_button_command)
        video_button.pack(side=RIGHT)

    # TODO: Create methods for each button to create it's own object type
    # TODO: Figure out warning from IntelliJ IDEA...

    # returns directory selected from file dialog
    def directory_button_command(self):
        path_to_directory = askdirectory()
        chosen_directory = directory.Directory(path_to_directory)
        return chosen_directory

    # returns video selected from file dialog
    def video_button_command(self):
        path_to_video = askopenfilename()
        chosen_video = video.Video(path_to_video)
        return chosen_video

if __name__ == '__main__':
    SplashScreen().mainloop()
