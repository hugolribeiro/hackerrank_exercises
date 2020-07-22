#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the staircase function below.
def staircase(n):
    for step in range(1, n + 1):
        spaces = n - step
        print(f'{" " * spaces}{"#" * step} ')


staircase(6)
# if __name__ == '__main__':
#    n = int(input())

#    staircase(n)
