import math
import os
import random
import re
import sys


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5
    liked = 0
    cumulative = 0
    for day in range(0, n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     result = viralAdvertising(n)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
