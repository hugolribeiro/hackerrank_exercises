import math
import os
import random
import re
import sys


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    amount_bdays = 0
    for number in range(i, j + 1):
        reverse_number = int(str(number)[::-1])
        result = (abs(number - reverse_number) % k)
        if result == 0:
            amount_bdays += 1
    return amount_bdays

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     ijk = input().split()
#
#     i = int(ijk[0])
#
#     j = int(ijk[1])
#
#     k = int(ijk[2])
#
#     result = beautifulDays(i, j, k)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
