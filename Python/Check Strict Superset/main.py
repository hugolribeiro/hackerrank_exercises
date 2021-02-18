# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(input().split())
amount_sets = int(input())
flag = True
for _ in range(0, amount_sets):
    actual_set = set(input().split())
    if not set_a.issuperset(actual_set):
        flag = False
        break
print(flag)
