def miniMaxSum(arr):
    sum_all = sum(arr)
    max_sum = sum_all - min(arr)
    min_sum = sum_all - max(arr)
    min_max = [min_sum, max_sum]
    return min_max


# Test 1
arr1 = [1, 3, 5, 7, 9]
min_max = miniMaxSum(arr1)
min_sum1 = min_max[0]
max_sum1 = min_max[1]
answer_min1 = 16
answer_max1 = 24
if min_sum1 == answer_min1 and max_sum1 == answer_max1:
    print(f'Test number 1 \nExpected Output: {answer_min1} {answer_max1}\nThe output: {min_sum1} {max_sum1} \n\033['
          f'0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer_min1} {answer_max1}\nThe output: {min_sum1} {max_sum1} \n\033['
          f'0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
arr2 = [1, 2, 3, 4, 5]
min_max = miniMaxSum(arr2)
min_sum2 = min_max[0]
max_sum2 = min_max[1]
answer_min2 = 10
answer_max2 = 14
if min_sum2 == answer_min2 and max_sum2 == answer_max2:
    print(f'Test number 2 \nExpected Output: {answer_min2} {answer_max2}\nThe output: {min_sum2} {max_sum2} \n\033['
          f'0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer_min2} {answer_max2}\nThe output: {min_sum2} {max_sum2} \n\033['
          f'0;31;1mWRONG\033[m')

# Test 3
arr3 = [15, 33, 4, 8, 33]
min_max = miniMaxSum(arr3)
min_sum3 = min_max[0]
max_sum3 = min_max[1]
answer_min3 = 60
answer_max3 = 89
if min_sum3 == answer_min3 and max_sum3 == answer_max3:
    print(f'Test number 3 \nExpected Output: {answer_min3} {answer_max3}\nThe output: {min_sum3} {max_sum3} \n\033['
          f'0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer_min3} {answer_max3}\nThe output: {min_sum3} {max_sum3} \n\033['
          f'0;31;1mWRONG\033[m')

# Test 4
arr4 = [5, 8, 8, 5, 7]
min_max = miniMaxSum(arr4)
min_sum4 = min_max[0]
max_sum4 = min_max[1]
answer_min4 = 25
answer_max4 = 28
if min_sum4 == answer_min4 and max_sum4 == answer_max4:
    print(f'Test number 4 \nExpected Output: {answer_min4} {answer_max4}\nThe output: {min_sum4} {max_sum4} \n\033['
          f'0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer_min4} {answer_max4}\nThe output: {min_sum4} {max_sum4} \n\033['
          f'0;31;1mWRONG\033[m')

# Test 5
arr5 = [5, 5, 5, 5, 5]
min_max = miniMaxSum(arr5)
min_sum5 = min_max[0]
max_sum5 = min_max[1]
answer_min5 = 20
answer_max5 = 20
if min_sum5 == answer_min5 and max_sum5 == answer_max5:
    print(f'Test number 5 \nExpected Output: {answer_min5} {answer_max5}\nThe output: {min_sum5} {max_sum5} \n\033['
          f'0;32;1mTest OK\033[m')
else:
    print(f'Test number 5 \nExpected Output: {answer_min5} {answer_max5}\nThe output: {min_sum5} {max_sum5} \n\033['
          f'0;31;1mWRONG\033[m')
