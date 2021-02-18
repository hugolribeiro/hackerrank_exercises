# Enter your code here. Read input from STDIN. Print output to STDOUT
tests = int(input())
for test in range(0, tests):
    _, set_a = input(), set(input().split())
    _, next_set = input(), set(input().split())
    if set_a.issubset(next_set):
        print(True)
    else:
        print(False) 
