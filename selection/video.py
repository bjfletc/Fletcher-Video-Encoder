# Author: Brandon J. Fletcher
# Date  : Wednesday, Aug 22, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""video.py: When user selects to encode a video, this will return a video object."""

import os


class Video:
    def __init__(self, path_to_video):
        self.path_to_video = path_to_video

    # return size of video in MB or GB
    def file_size(self):
        video_file_size_in_bytes = os.path.getsize(self.path_to_video)
        video_file_size_in_megabytes = video_file_size_in_bytes / 1000000.00

        if video_file_size_in_megabytes >= 1000:
            video_file_size_in_gigabytes = video_file_size_in_megabytes / 1000.00
            return video_file_size_in_gigabytes
        else:
            return video_file_size_in_megabytes


if __name__ == '__main__':
    test_video_0 = Video('W:\Brandon J. Fletcher\Videos\YouTube\MKBHD\Talking Tech with Elon Musk!.mp4')
    print(str(test_video_0.file_size()))
