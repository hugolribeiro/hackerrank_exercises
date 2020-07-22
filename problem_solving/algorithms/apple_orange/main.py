import math
import os


# import random
# import re
# import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    fallen_apples = []
    fallen_oranges = []
    apples_hit_house = 0
    oranges_hit_house = 0
    for apple in apples:
        fallen_apple = apple + a
        fallen_apples.append(fallen_apple)
    for fallen_apple in fallen_apples:
        if s <= fallen_apple <= t:
            apples_hit_house += 1
    for orange in oranges:
        fallen_orange = orange + b
        fallen_oranges.append(fallen_orange)
    for fallen_orange in fallen_oranges:
        if s <= fallen_orange <= t:
            oranges_hit_house += 1
    print(apples_hit_house)
    print(oranges_hit_house)


################################
# if __name__ == '__main__':
#     st = input().split()
#
#     s = int(st[0])
#
#     t = int(st[1])
#
#     ab = input().split()
#
#     a = int(ab[0])
#
#     b = int(ab[1])
#
#     mn = input().split()
#
#     m = int(mn[0])
#
#     n = int(mn[1])
#
#     apples = list(map(int, input().rstrip().split()))
#
#     oranges = list(map(int, input().rstrip().split()))
#
#     countApplesAndOranges(s, t, a, b, apples, oranges)
