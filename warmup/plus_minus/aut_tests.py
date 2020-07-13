def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    total_numbers = len(arr)
    for element in arr:
        if element > 0:
            positives += 1
        elif element < 0:
            negatives += 1
        elif element == 0:
            zeros += 1
    pos_fraction = (positives/total_numbers)
    neg_fraction = (negatives/total_numbers)
    zeros_fraction = (zeros/total_numbers)
    return pos_fraction, neg_fraction, zeros_fraction


# Test 1
arr1 = [1, 1, 0, -1, -1]
result1 = plusMinus(arr1)
positive_fraction1 = result1[0]
negative_fraction1 = result1[1]
zero_fraction1 = result1[2]
answer_positive1 = 0.4
answer_negative1 = 0.4
answer_zero1 = 0.2
if positive_fraction1 == answer_positive1 and negative_fraction1 == answer_negative1 and zero_fraction1 == answer_zero1:
    print(f'Test number 1 \nExpected Output: {answer_positive1} {answer_negative1} {answer_zero1}\nThe output: '
          f'{positive_fraction1} {negative_fraction1} {zero_fraction1}\n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer_positive1} {answer_negative1} {answer_zero1}\nThe output: '
          f'{positive_fraction1} {negative_fraction1} {zero_fraction1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
arr2 = [-4, 3, -9, 0, 4, 1]
result2 = plusMinus(arr2)
positive_fraction2 = round(result2[0], 6)
negative_fraction2 = round(result2[1], 6)
zero_fraction2 = round(result2[2], 6)
answer_positive2 = 0.500000
answer_negative2 = 0.333333
answer_zero2 = 0.166667
if positive_fraction2 == answer_positive2 and negative_fraction2 == answer_negative2 and zero_fraction2 == answer_zero2:
    print(f'Test number 2 \nExpected Output: {answer_positive2} {answer_negative2} {answer_zero2}\nThe output: '
          f'{positive_fraction2} {negative_fraction2} {zero_fraction2}\n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer_positive2} {answer_negative2} {answer_zero2}\nThe output: '
          f'{positive_fraction2} {negative_fraction2} {zero_fraction2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 3
arr3 = [4, -8, 0, 0, 0]
result3 = plusMinus(arr3)
positive_fraction3 = result3[0]
negative_fraction3 = result3[1]
zero_fraction3 = result3[2]
answer_positive3 = 0.2
answer_negative3 = 0.2
answer_zero3 = 0.6
if positive_fraction3 == answer_positive3 and negative_fraction3 == answer_negative3 and zero_fraction3 == answer_zero3:
    print(f'Test number 3 \nExpected Output: {answer_positive3} {answer_negative3} {answer_zero3}\nThe output: '
          f'{positive_fraction3} {negative_fraction3} {zero_fraction3}\n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer_positive3} {answer_negative1} {answer_zero3}\nThe output: '
          f'{positive_fraction3} {negative_fraction3} {zero_fraction3} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 1
arr4 = [0, 0, 0, 0, 0]
result4 = plusMinus(arr4)
positive_fraction4 = result4[0]
negative_fraction4 = result4[1]
zero_fraction4 = result4[2]
answer_positive4 = 0.0
answer_negative4 = 0.0
answer_zero4 = 1.0
if positive_fraction4 == answer_positive4 and negative_fraction4 == answer_negative4 and zero_fraction4 == answer_zero4:
    print(f'Test number 4 \nExpected Output: {answer_positive4} {answer_negative4} {answer_zero4}\nThe output: '
          f'{positive_fraction4} {negative_fraction4} {zero_fraction4}\n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 4 \nExpected Output: {answer_positive4} {answer_negative4} {answer_zero4}\nThe output: '
          f'{positive_fraction4} {negative_fraction4} {zero_fraction4} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)
