from main import diagonalDifference

arr1 = [[11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]]
result1 = diagonalDifference(arr1)
answer1 = 15
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
arr2 = [[6, 7, 8],
        [5, 2, 12],
        [10, 9, -10]]
result2 = diagonalDifference(arr2)
answer2 = 22
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
arr3 = [[-5, 23, 4],
        [8, 15, 6],
        [23, 0, 5]]
result3 = diagonalDifference(arr3)
answer3 = 27
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 4
arr4 = [[36, 23, -4],
        [41, -50, 6],
        [10, -15, 7]]
result4 = diagonalDifference(arr4)
answer4 = 37
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')
