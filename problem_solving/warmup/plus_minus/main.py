#import math
#import os
#import random
#import re
#import sys


def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    total_numbers = len(arr)
    for element in arr:
        if element > 0:
            positives += 1
        elif element < 0:
            negatives += 1
        elif element == 0:
            zeros += 1
    print(positives/total_numbers)
    print(negatives/total_numbers)
    print(zeros/total_numbers)


# if __name__ == '__main__':
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     plusMinus(arr)