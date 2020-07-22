# Programmer: Hugo Leça Ribeiro
# Date: 07/21/2020

from main import divisibleSumPairs

# Test 1
n1 = 6
k1 = 3
r1 = [1, 3, 2, 6, 1, 2]
result1 = divisibleSumPairs(n1, k1, r1)
answer1 = 5
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
n2 = 6
k2 = 5
r2 = [1, 2, 3, 4, 5, 6]
result2 = divisibleSumPairs(n2, k2, r2)
answer2 = 3
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
n3 = 4
k3 = 5
r3 = [2, 3, 5, 5]
result3 = divisibleSumPairs(n3, k3, r3)
answer3 = 2
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
