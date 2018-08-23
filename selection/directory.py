# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 22, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""directory.py: When user selects to encode an entire directory, this will return a list of video objects."""
from selection.video import Video
# TODO(2.0): see if I can add similar imports to a package as to not add them in each class call
import os
from byte_calculator import ByteCalculator
# TODO(1.0): create a class variable for size that can be saved from videos


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
        # TODO(1.1): set the class variable when iterating through videos...
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

        # COMPLETED(2.0): want to change so I am not iterating twice in the same class...
        for vid in videos_in_this_directory:
            total_bytes_of_videos += os.path.getsize(vid.complete_path())

        # COMPLETED(1.0): create class that converts from bytes to MB & GB
        # COMPLETED(1.1): as to avoid code reuse in directory and video
        total_size_of_directory_in_bytes = ByteCalculator(total_bytes_of_videos)
        size_of_directory = total_size_of_directory_in_bytes.total()
        return size_of_directory


if __name__ == '__main__':
    test_directory_0 = Directory('W:\Brandon J. Fletcher\Videos\YouTube\MKBHD')
    print(test_directory_0.name())
    print(test_directory_0.size())

    # iterate through videos
    test_directory_0_videos = test_directory_0.videos()
    print('<----------------------TESTING LIST OF VIDEO OBJECTS----------------------------->')
    for video in test_directory_0_videos:
        print('[' + video.title() + ' , ' + video.file_size() + ' , ' + video.format() + ']')
