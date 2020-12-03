from main import angryProfessor

# Test 1
k, a = 3, [-1, -3, 4, 2]
result1 = angryProfessor(k, a)
answer1 = 'YES'
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
k, a = 2, [0, -1, 2, 1]
result2 = angryProfessor(k, a)
answer2 = 'NO'
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)
