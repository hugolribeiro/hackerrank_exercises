# Programmer: Hugo Leça Ribeiro
# Date: 07/23/2020


def bonAppetit(bill, k, b):
    ana_amount = (sum(bill) - bill[k]) // 2
    if b == ana_amount:
        return 'Bon Appetit'
    else:
        difference = b - ana_amount
        return difference


# Test 1
k1 = 1
bill1 = [3, 10, 2, 9]
b1 = 12
result1 = bonAppetit(bill1, k1, b1)
answer1 = 5
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
k2 = 1
bill2 = [3, 10, 2, 9]
b2 = 7
result2 = bonAppetit(bill2, k2, b2)
answer2 = 'Bon Appetit'
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

# Test 3
k3 = 2
bill3 = [3, 10, 2, 9, 6, 6]
b3 = 17
result3 = bonAppetit(bill3, k3, b3)
answer3 = 'Bon Appetit'
if result3 == answer3:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 3 \nExpected Output: {answer3}\nThe output: {result3} \n\033[0;31;1mWRONG\033[m')
