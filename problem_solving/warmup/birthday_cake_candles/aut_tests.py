from main import birthdayCakeCandles

# Test 1
test1 = [1, 1, 2]
result1 = birthdayCakeCandles(test1)
answer1 = 1
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
test2 = [3, 3, 3, 3, 4]
result2 = birthdayCakeCandles(test2)
answer2 = 1
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
test3 = [3, 2, 1, 3]
result3 = birthdayCakeCandles(test3)
answer3 = 2
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 4
test4 = [500, 485, 25, 26, 44, 500]
result4 = birthdayCakeCandles(test4)
answer4 = 2
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 5
test5 = [8, 2, 3, 4, 5, 10, 8, 7, 12]
result5 = birthdayCakeCandles(test5)
answer5 = 1
if result5 == answer5:
    print(f'Test number 5 \nExpected Output: {answer5}\nThe output: {result5} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 5 \nExpected Output: {answer5}\nThe output: {result5} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 6
test6 = [10, 10, 10, 10, 6, 4, 2]
result6 = birthdayCakeCandles(test6)
answer6 = 4
if result6 == answer6:
    print(f'Test number 6 \nExpected Output: {answer6}\nThe output: {result6} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 6 \nExpected Output: {answer6}\nThe output: {result6} \n\033[0;31;1mWRONG\033[m')
