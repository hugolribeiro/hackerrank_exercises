# Enter your code here. Read input from STDIN. Print output to STDOUT
values = input().split()
x = values[0]
k = values[1]
expression = input().replace('x', x)

if eval(expression) == int(k):
    print(True)
else:
    print(False)
