# import math
# import os
# import random
# import re
# import sys


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    arrived_on = 0
    for student_time in a:
        if student_time <= 0:
            arrived_on += 1
    if arrived_on >= k:
        return 'NO'
    else:
        return 'YES'


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         nk = input().split()
#
#         n = int(nk[0])
#
#         k = int(nk[1])
#
#         a = list(map(int, input().rstrip().split()))
#
#         result = angryProfessor(k, a)
#
#         fptr.write(result + '\n')
#
#     fptr.close()