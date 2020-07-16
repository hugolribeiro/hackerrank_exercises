# Programmer: Hugo Leça Ribeiro
# Date: 07/16/2020

# import math
# import os
# import random
# import re
# import sys

# Complete the breakingRecords function below.


def breakingRecords(scores):
    highest_score = scores[0]
    lowest_score = scores[0]
    times_high = 0
    times_worst = 0
    for score in range(1, len(scores)):
        if scores[score] > highest_score:
            highest_score = scores[score]
            times_high += 1
        elif scores[score] < lowest_score:
            lowest_score = scores[score]
            times_worst += 1
    return [times_high, times_worst]


#################################################
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     scores = list(map(int, input().rstrip().split()))
#
#     result = breakingRecords(scores)
#
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
