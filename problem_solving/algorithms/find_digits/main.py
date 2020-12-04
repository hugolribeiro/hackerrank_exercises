# import math
# import os
# import random
# import re
# import sys


# Complete the findDigits function below.
def findDigits(n):
    string_number = str(n)
    divisors = 0
    for digit in string_number:
        if digit == '0':
            continue
        if n % int(digit) == 0:
            divisors += 1
    return divisors


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         n = int(input())
#
#         result = findDigits(n)
#
#         fptr.write(str(result) + '\n')
#
#     fptr.close()
