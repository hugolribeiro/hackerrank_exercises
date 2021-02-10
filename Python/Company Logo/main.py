#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    output = {}
    s_ordered = sorted(list(s))
    for numbers in range(0, 3):
        letter = max(s_ordered, key=s_ordered.count)
        amount_letter = s_ordered.count(letter)
        output[letter] = amount_letter
        s_ordered = (''.join(s_ordered)).replace(letter, '')
    for key, value in output.items():
        print(key, value)
            
            
# Another solution:
# s = input() list1 = list(s) list1.sort() 
# counter=collections.Counter(list1).most_common(3) for i,j in counter: print(i,j)
