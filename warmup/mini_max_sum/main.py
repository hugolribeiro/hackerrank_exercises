# import math
# import os
# import random
# import re
# import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_all = sum(arr)
    max_sum = sum_all - min(arr)
    min_sum = sum_all - max(arr)
    print(f'{min_sum} {max_sum}')


#################################################
# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))
#
#     miniMaxSum(arr)
