# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = input()
set1 = set(map(int, input().split()))
n2 = input()
set2 = set(map(int, input().split()))
set3 = set()
set3.update(set1.difference(set2))
set3.update(set2.difference(set1))
lista = sorted(list(set3))

for number in lista:
    print(number)
