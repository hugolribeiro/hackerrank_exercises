# Programmer: Hugo Leça Ribeiro
# Date: 07/27/2020

from main import getMoneySpent

# Test 1
keyboards1 = [40, 50, 60]
drives1 = [5, 8, 12]
b1 = 60
result1 = getMoneySpent(keyboards1, drives1, b1)
answer1 = 58
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
keyboards2 = [3, 1]
drives2 = [5, 2, 8]
b2 = 10
result2 = getMoneySpent(keyboards2, drives2, b2)
answer2 = 9
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

# Test 3
keyboards3 = [4]
drives3 = [5]
b3 = 5
result3 = getMoneySpent(keyboards3, drives3, b3)
answer3 = -1
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
