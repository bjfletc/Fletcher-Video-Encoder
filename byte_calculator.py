# Author: Brandon J. Fletcher
# Created  : Wednesday, Aug 23, 2018
# E-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc

"""byte_calculator.py is to be used in selection project to return the file size"""
from decimal import Decimal


class ByteCalculator:
    def __init__(self, amount_of_bytes=0):
        self.amount_of_bytes = amount_of_bytes

    def to_megabytes(self):
        bytes_to_megabytes = Decimal(self.amount_of_bytes / 1024 / 1024)
        return bytes_to_megabytes

    def to_gigabytes(self):
        bytes_to_gigabytes = Decimal(self.to_megabytes() / 1024)
        return bytes_to_gigabytes

    def total(self):
        if self.to_megabytes() < 1000:
            return str(round(self.to_megabytes(), 2)) + ' Megabytes'
        else:
            return str(round(self.to_gigabytes(), 2)) + ' Gigabytes'


if __name__ == '__main__':
    test_bytes_0 = ByteCalculator(1000000)
    print(test_bytes_0.total())
