# Enter your code here. Read input from STDIN. Print output to STDOUT
length = input()
main_set = set(map(int, input().split()))
for operation in range(0, int(input())):
    operation_name = (input().split())[0]
    numbers = set(map(int, input().split()))
    eval(f'main_set.{operation_name}(numbers)')
print(sum(main_set))
