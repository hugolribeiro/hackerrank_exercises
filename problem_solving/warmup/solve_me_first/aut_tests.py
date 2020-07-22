from main import solveMeFirst


# Test 1
a1 = 2
b1 = 3
result1 = solveMeFirst(a1, b1)
answer1 = 5
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
a2 = 20
b2 = 31
result2 = solveMeFirst(a2, b2)
answer2 = 51
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
a3 = 17
b3 = 3
result3 = solveMeFirst(a3, b3)
answer3 = 20
if result3 == answer3:
    print(f'Test number 1 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 4
a4 = 15
b4 = 16
result4 = solveMeFirst(a4, b4)
answer4 = 31
if result4 == answer4:
    print(f'Test number 1 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')
