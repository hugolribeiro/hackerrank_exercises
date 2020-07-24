# Programmer: Hugo Leça Ribeiro
# Date: 07/24/2020

from main import countingValleys

# Test 1
n1 = 8
s1 = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
result1 = countingValleys(n1, s1)
answer1 = 1
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
n2 = 12
s2 = ['D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D']
result2 = countingValleys(n2, s2)
answer2 = 2
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

# Test 3
n3 = 8
s3 = ['U', 'U', 'D', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'D']
result3 = countingValleys(n3, s3)
answer3 = 2
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
