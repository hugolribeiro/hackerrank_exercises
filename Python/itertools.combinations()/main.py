# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

word, limit_size = input().split()
word = sorted(word)
limit_size = int(limit_size)

for size in range(1, limit_size+1):
    tuples = combinations(word, size)
    for combination in tuples:
        print(''.join(combination))
