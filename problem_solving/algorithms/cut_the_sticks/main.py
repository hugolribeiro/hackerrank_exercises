#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = [len(arr)]
    while len(arr) > 1:
        minor_element = min(arr)
        new_array = []
        for number in arr:
            difference = number - minor_element
            if difference > 0:
                new_array.append(difference)
        arr = new_array
        length = len(arr)
        if length > 0:
            result.append(length)
    return result


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     result = cutTheSticks(arr)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()