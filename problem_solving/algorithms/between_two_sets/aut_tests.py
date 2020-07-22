# Programmer: Hugo Leça Ribeiro
# Date: 07/17/2020

from main import getTotalX

# Test 1
a1 = [2, 4]
b1 = [16, 32, 96]
result1 = getTotalX(a1, b1)
answer1 = 3
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
a2 = [2, 6]
b2 = [24, 36]
result2 = getTotalX(a2, b2)
answer2 = 2
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')
