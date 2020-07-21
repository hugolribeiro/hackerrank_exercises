#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds = [0, 0, 0, 0, 0]
    for bird in arr:
        birds[bird-1] += 1
    highest_value = max(birds)
    result = birds.index(highest_value) + 1
    return result


#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    arr_count = int(input().strip())

#    arr = list(map(int, input().rstrip().split()))

#    result = migratoryBirds(arr)

#    fptr.write(str(result) + '\n')

#    fptr.close()


