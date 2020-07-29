# Programmer: Hugo Leça Ribeiro
# Date: 07/29/2020

from main import pickingNumbers

# Test 1
a1 = [4, 6, 5, 3, 3, 1]
result1 = pickingNumbers(a1)
answer1 = 3
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
a2 = [1, 2, 2, 3, 1, 2]
result2 = pickingNumbers(a2)
answer2 = 5
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
a3 = [7, 6, 4, 5, 6, 5, 6, 3, 3, 2, 1, 5, 6, 4, 7, 8, 9]
result3 = pickingNumbers(a3)
answer3 = 7
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
