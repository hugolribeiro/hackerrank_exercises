#import math
#import os
#import random
#import re
#import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    total_left = 0
    total_right = 0
    amount_rows = len(arr)
    index_right = amount_rows - 1

    for vector in arr:
        index_row = arr.index(vector)
        total_left += vector[index_row]
        total_right += vector[index_right]
        index_right -= 1
    absolute_diff = abs(total_right - total_left)
    return absolute_diff


#####################################################
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     arr = []
#
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#
#     result = diagonalDifference(arr)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()