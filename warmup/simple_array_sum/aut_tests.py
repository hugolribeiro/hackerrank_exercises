from main import simpleArraySum

test1 = [1, 2, 3]
result1 = simpleArraySum(test1)
answer1 = 6
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
test2 = [1, 2, 3, 4, 10, 11]
result2 = simpleArraySum(test2)
answer2 = 31
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
test3 = [15, 35, 41, 5, 10]
result3 = simpleArraySum(test3)
answer3 = 106
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 4
test4 = [7, 19, 10, 85, 31, 14, 32, 21]
result4 = simpleArraySum(test4)
answer4 = 219
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')