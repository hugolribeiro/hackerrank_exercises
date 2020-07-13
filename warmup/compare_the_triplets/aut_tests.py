from main import compareTriplets

a1 = [1, 2, 3]
b1 = [3, 2, 1]
result1 = compareTriplets(a1, b1)
answer1 = [1, 1]
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
a2 = [5, 6, 7]
b2 = [3, 6, 10]
result2 = compareTriplets(a2, b2)
answer2 = [1, 1]
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
a3 = [10, 20, 30]
b3 = [7, 19, 18]
result3 = compareTriplets(a3, b3)
answer3 = [3, 0]
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 4
a4 = [17, 28, 30]
b4 = [99, 16, 8]
result4 = compareTriplets(a4, b4)
answer4 = [2, 1]
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')
