# Programmer: Hugo Leça Ribeiro
# Date: 07/15/2020

from main import kangaroo


x1, v1, x2, v2 = 0, 3, 4, 2
result1 = kangaroo(x1, v1, x2, v2)
answer1 = 'YES'
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
x1, v1, x2, v2 = 0, 2, 5, 3
result2 = kangaroo(x1, v1, x2, v2)
answer2 = 'NO'
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
x1, v1, x2, v2 = 2, 1, 3, 2
result3 = kangaroo(x1, v1, x2, v2)
answer3 = 'NO'
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 4
x1, v1, x2, v2 = 1, 5, 7, 2
result4 = kangaroo(x1, v1, x2, v2)
answer4 = 'YES'
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')

# Test 5
x1, v1, x2, v2 = 40, 2, 54, 2
result4 = kangaroo(x1, v1, x2, v2)
answer4 = 'NO'
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')


