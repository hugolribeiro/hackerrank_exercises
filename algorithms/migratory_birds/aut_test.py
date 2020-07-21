# Programmer: Hugo Leça Ribeiro
# Date: 07/21/2020

from main import migratoryBirds

# Test 1
arr1 = [1, 4, 4, 4, 5, 3]
result1 = migratoryBirds(arr1)
answer1 = 4
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
arr2 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
result2 = migratoryBirds(arr2)
answer2 = 3
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
arr3 = [4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 1, 2, 4]
result3 = migratoryBirds(arr3)
answer3 = 2
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
