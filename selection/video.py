# Author: Brandon J. Fletcher
# Date  : Wednesday, Aug 22, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""video.py: When user selects to encode a video, this will return a video object."""

import os
from decimal import Decimal     # used for file_size() method


class Video:
    def __init__(self, path_to_video):
        self.path_to_video = path_to_video

    # return complete path to video
    def complete_path(self):
        return self.path_to_video

    # separate the video from the path
    def title(self):
        # current build is supporting Windows 10...
        # future builds will need logic to determine
        # if on macOS or Linux...
        end_of_path = self.path_to_video.rfind('\\')
        title = self.path_to_video[(end_of_path + 1):]
        return title

    # return size of video in MB or GB
    def file_size(self):
        video_file_size_in_bytes = os.path.getsize(self.path_to_video)
        video_file_size_in_megabytes = Decimal(video_file_size_in_bytes / 1000000.00)

        if video_file_size_in_megabytes >= 1000:
            video_file_size_in_gigabytes = Decimal(video_file_size_in_megabytes / 1000.00)
            return str(round(video_file_size_in_gigabytes, 2)) + ' gigabytes'
        else:
            return str(round(video_file_size_in_megabytes, 2)) + ' megabytes'

    # determine starting format of video
    def format(self):
        video = self.title()
        format_type = video[video.rfind('.'):]
        return format_type


if __name__ == '__main__':
    test_video_0 = Video('W:\Brandon J. Fletcher\Videos\YouTube\MKBHD\Talking Tech with Elon Musk!.mp4')
    # ^ Great video BTW, should check it out if you haven't yet: https://youtu.be/MevKTPN4ozw
    print(test_video_0.file_size())
    print(test_video_0.title())
    print(test_video_0.format())