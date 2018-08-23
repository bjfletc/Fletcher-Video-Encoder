# Author: Brandon J. Fletcher
# Date  : Wednesday, Aug 22, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""directory.py: When user selects to encode an entire directory, this will return a list of video objects."""
from selection.video import Video
import os


class Directory:
    def __init__(self, path_to_directory):
        self.path_to_directory = path_to_directory

    # specify the name of the folder
    def name(self):
        index_of_end_of_path_to_directory = (self.path_to_directory.rfind('\\')) + 1
        name_of_directory = self.path_to_directory[index_of_end_of_path_to_directory:]
        return name_of_directory

    # return list of Video objects
    def videos(self):
        names_of_videos_in_directory = os.listdir(self.path_to_directory)
        list_of_video = []

        # create a list of Video objects
        for file in names_of_videos_in_directory:
            list_of_video.append(Video(self.path_to_directory + '\\' + file))

        return list_of_video


if __name__ == '__main__':
    test_directory_0 = Directory('W:\Brandon J. Fletcher\Videos\YouTube\MKBHD')
    print(test_directory_0.name())

    # iterate through videos
    test_directory_0_videos = test_directory_0.videos()
    print('<----------------------TESTING LIST OF VIDEO OBJECTS----------------------------->')
    for video in test_directory_0_videos:
        print('[' + video.title() + ' , ' + video.file_size() + ' , ' + video.format() + ']')
