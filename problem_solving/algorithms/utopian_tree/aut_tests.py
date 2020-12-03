from main import utopianTree

# Test 1
n = 4
result1 = utopianTree(n)
answer1 = 7
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
n = 0
result2 = utopianTree(n)
answer2 = 1
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
n = 5
result3 = utopianTree(n)
answer3 = 14
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 4
n = 1
result4 = utopianTree(n)
answer4 = 2
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')

# Test 5
n = 2
result5 = utopianTree(n)
answer5 = 3
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')