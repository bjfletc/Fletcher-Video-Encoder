# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""splash_screen.py: When the program is run, will be the screen that they see first."""
from tkinter import *
from tkinter.filedialog import askopenfile, askdirectory


class SplashScreen:

    def name(self):
        return 'Hello GUI World!'


if __name__ == '__main__':
    test_GUI = SplashScreen()
    print(test_GUI.name())