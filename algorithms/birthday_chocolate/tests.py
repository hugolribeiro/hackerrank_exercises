# Programmer: Hugo Leça Ribeiro
# Date: 07/19/2020

from main import birthday

# Test 1
s1 = [1, 2, 1, 3, 2]
d1 = 3
m1 = 2
result1 = birthday(s1, d1, m1)
answer1 = 2
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
s2 = [1, 1, 1, 1, 1, 1]
d2 = 3
m2 = 2
result2 = birthday(s2, d2, m2)
answer2 = 0
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

# Test 3
s3 = [4]
d3 = 4
m3 = 1
result3 = birthday(s3, d3, m3)
answer3 = 1
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
