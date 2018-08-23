# Author: Brandon J. Fletcher
# Date  : Wednesday, Aug 22, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""directory.py: When user selects to encode an entire directory, this will return a list of video objects."""
# from tkinter.filedialog import askdirectory


class Directory:
    def __init__(self, path_to_directory):
        self.path_to_directory = path_to_directory

    def name(self):
        index_of_end_of_path_to_directory = (self.path_to_directory.rfind('\\')) + 1
        name_of_directory = self.path_to_directory[index_of_end_of_path_to_directory:]
        return name_of_directory


if __name__ == '__main__':
    # test if module is ran as a script
    test_directory_0 = Directory('W:\Brandon J. Fletcher\Videos\YouTube\MKBHD')
    print(test_directory_0.name())
