# Programmer: Hugo Leça Ribeiro
# Date: 07/27/2020

from main import catAndMouse

# Test 1
x1 = 22
y1 = 75
z1 = 70
result1 = catAndMouse(x1, y1, z1)
answer1 = 'Cat B'
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
x2 = 33
y2 = 86
z2 = 59
result2 = catAndMouse(x2, y2, z2)
answer2 = 'Cat A'
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

# Test 3
x3 = 5
y3 = 15
z3 = 10
result3 = catAndMouse(x3, y3, z3)
answer3 = 'Mouse C'
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
