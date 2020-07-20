# import math
# import os
# import random
# import re
# import sys

# Programmer: Hugo Leça Ribeiro
# Date: 07/19/2020
# Complete the birthday function below.


def birthday(s, d, m):
    times = 0
    for index in range(0, len(s) + 1 - m):
        total = 0
        for count in range(index, index + m):
            total += s[count]
            if total > d:
                break
        if total == d:
            times += 1
    return times

# if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    n = int(input().strip())

#    s = list(map(int, input().rstrip().split()))

#    dm = input().rstrip().split()

#   d = int(dm[0])

#    m = int(dm[1])

#    result = birthday(s, d, m)

#    fptr.write(str(result) + '\n')

#    fptr.close()
