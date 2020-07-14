from main import gradingStudents


test1 = [73, 67, 38, 33]
result1 = gradingStudents(test1)
answer1 = [75, 67, 40, 33]
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
test2 = [25, 28, 38, 41, 99]
result2 = gradingStudents(test2)
answer2 = [25, 28, 40, 41, 100]
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
test3 = [15, 95, 90, 91, 92]
result3 = gradingStudents(test3)
answer3 = [15, 95, 90, 91, 92]
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 4
test4 = [50, 62, 71, 87, 93]
result4 = gradingStudents(test4)
answer4 = [50, 62, 71, 87, 95]
if result4 == answer4:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer4}\nThe output: {result4} \n\033[0;31;1mWRONG\033[m')

