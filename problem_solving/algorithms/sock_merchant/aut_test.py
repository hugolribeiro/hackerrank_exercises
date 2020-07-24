# Programmer: Hugo Leça Ribeiro
# Date: 07/23/2020
from main import sockMerchant

# Test 1
ar1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n1 = 9
result1 = sockMerchant(n1, ar1)
answer1 = 3
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
ar2 = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
n2 = 9
result2 = sockMerchant(n2, ar2)
answer2 = 4
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

# Test 3
ar3 = [7, 7, 3, 3, 2, 7, 2, 1, 7]
n3 = 9
result3 = sockMerchant(n3, ar3)
answer3 = 4
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
