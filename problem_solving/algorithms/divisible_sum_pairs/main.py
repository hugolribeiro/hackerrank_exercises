#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the divisibleSumPairs function below.


def divisibleSumPairs(n, k, ar):
    valid_pairs = 0
    amount = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            amount = ar[i] + ar[j]
            if amount % k == 0:
                valid_pairs += 1
    return valid_pairs

# if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    nk = input().split()

#    n = int(nk[0])

#    k = int(nk[1])

#    ar = list(map(int, input().rstrip().split()))

#    result = divisibleSumPairs(n, k, ar)

#   fptr.write(str(result) + '\n')

#   fptr.close()
