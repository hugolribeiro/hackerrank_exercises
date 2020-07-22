# import math
# import os
# import random
# import re
# import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tallest = max(ar)
    candles_blowout = ar.count(tallest)
    return candles_blowout


#################################################
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     ar_count = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = birthdayCakeCandles(ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

birthdayCakeCandles([1, 3, 4, 4, 4, 5])
# Automation Test - retire '#' to work
