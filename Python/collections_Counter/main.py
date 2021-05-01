# Programmer Hugo Leça Ribeiro

from collections import Counter

n_shoes = int(input())
shoes = list(map(int, input().split(' ')))
customers = int(input())
shoes = Counter(shoes)
total_money = 0
for customer in range(0, customers):
    number, price = list(map(int, input().split(' ')))
    if shoes[number] > 0:
        shoes[number] -= 1
        total_money += price
print(total_money)