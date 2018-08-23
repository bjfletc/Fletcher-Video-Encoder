# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 22, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""directory.py: When user selects to encode an entire directory, this will return a list of video objects."""
from selection.video import Video
# TODO(3.0): see if I can add similar imports to a package as to not add them in each class call
import os
from decimal import Decimal
# TODO(2.1): create a class variable for size that can be saved from videos


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
        # TODO(2.2): set the class variable when iterating through videos...
        names_of_videos_in_directory = os.listdir(self.path_to_directory)
        list_of_video = []

        # create a list of Video objects
        for file in names_of_videos_in_directory:
            list_of_video.append(Video(self.path_to_directory + '\\' + file))

        return list_of_video

    # return amount of space dir uses on the disk
    def size(self):
        videos_in_this_directory = self.videos()
        total_bytes_of_videos = 0

        # TODO(2.0): want to change so I am not iterating twice in the same class...
        for vid in videos_in_this_directory:
            total_bytes_of_videos += os.path.getsize(vid.complete_path())

        directory_size_in_megabytes = Decimal(total_bytes_of_videos / 1000000.00)

        # TODO(1.0): create class that converts from bytes to MB & GB
        # TODO(1.1): as to avoid code reuse in directory and video
        if directory_size_in_megabytes >= 1000:
            directory_size_in_gigabytes = Decimal(directory_size_in_megabytes / 1000.00)
            return str(round(directory_size_in_gigabytes, 2)) + ' gigabytes'
        else:
            return str(round(directory_size_in_megabytes, 2)) + ' megabytes'


if __name__ == '__main__':
    test_directory_0 = Directory('W:\Brandon J. Fletcher\Videos\YouTube\MKBHD')
    print(test_directory_0.name())
    print(test_directory_0.size())

    # iterate through videos
    test_directory_0_videos = test_directory_0.videos()
    print('<----------------------TESTING LIST OF VIDEO OBJECTS----------------------------->')
    for video in test_directory_0_videos:
        print('[' + video.title() + ' , ' + video.file_size() + ' , ' + video.format() + ']')
