#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    words = {}
    ok = True
    for word in magazine:
        if words.get(word, None):
            words[word] += 1
        else:
            words[word] = 1
    for word in note:
        if words.get(word, None):
            words[word] -= 1
        else:
            ok = False
            break
    if ok:
        print('Yes')
    else:
        print('No')


# def checkMagazine(magazine, note):
#     ok = True
#     if len(magazine) < len(note):
#         ok = False
#     else:
#         for note_word in note:
#             if note_word in magazine:
#                 magazine.remove(note_word)
#             else:
#                 ok = False
#                 break
#     if ok:
#         print('Yes')
#     else:
#         print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
