# Programmer: Hugo Leça Ribeiro
# Date: 07/16/2020

from main import breakingRecords


scores1 = [10, 5, 20, 20, 4, 5, 2, 25, 1]
result1 = breakingRecords(scores1)
answer1 = [2, 4]
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
scores2 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
result2 = breakingRecords(scores2)
answer2 = [4, 0]
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
scores3 = [10, 5, 10, 25, 20, 4, 7, 8, 25, 1, 30, 21]
result3 = breakingRecords(scores3)
answer3 = [2, 3]
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
