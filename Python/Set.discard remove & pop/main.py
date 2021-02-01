n = int(input())
s = set(map(int, input().split()))
commands = int(input())
for command in range(0, commands):
    full_command = input().split(' ')
    if full_command[0] == 'pop':
        s.pop()
    else:
        eval(f's.{full_command[0]}({full_command[1]})')
print(sum(s))
