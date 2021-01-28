from itertools import permutations

word, num = input().strip().split()
list_combination = sorted(list(permutations(word, int(num))))

for combination in list_combination:
    print("".join(list(combination)))
