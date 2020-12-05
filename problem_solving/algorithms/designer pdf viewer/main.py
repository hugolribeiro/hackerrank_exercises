# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    taller = 0
    length = len(word)
    word = list(set(word))
    for letter in word:
        index = alpha.index(letter)
        height = h[index]
        if height > taller:
            taller = height
    result = (taller * length)
    return result

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     h = list(map(int, input().rstrip().split()))
#
#     word = input()
#
#     result = designerPdfViewer(h, word)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
