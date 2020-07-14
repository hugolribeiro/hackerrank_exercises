def countApplesAndOranges(s, t, a, b, apples, oranges):
    fallen_apples = []
    fallen_oranges = []
    apples_hit_house = 0
    oranges_hit_house = 0
    for apple in apples:
        fallen_apple = apple + a
        fallen_apples.append(fallen_apple)
    for fallen_apple in fallen_apples:
        if s <= fallen_apple <= t:
            apples_hit_house += 1
    for orange in oranges:
        fallen_orange = orange + b
        fallen_oranges.append(fallen_orange)
    for fallen_orange in fallen_oranges:
        if s <= fallen_orange <= t:
            oranges_hit_house += 1
    return [apples_hit_house, oranges_hit_house]


# Test 1
s = 7
t = 11
a = 5
b = 2
apples = [-2, 2, 1]
oranges = [5, -6]
result1 = countApplesAndOranges(s, t, a, b, apples, oranges)
answer1 = [1, 1]
if result1 == answer1:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 1 \nExpected Output: {answer1}\nThe output: {result1} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)

# Test 2
s = 5
t = 7
a = 2
b = 8
apples = [3, -2, 1, 2, -10, 4, 5, 6]
oranges = [3, 5, 4, 10, 15, -5, -6, -2, -3, -4]
result2 = countApplesAndOranges(s, t, a, b, apples, oranges)
answer2 = [3, 2]
if result2 == answer2:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;32;1mTest OK\033[m')
else:
    print(f'Test number 2 \nExpected Output: {answer2}\nThe output: {result2} \n\033[0;31;1mWRONG\033[m')

print('#' * 20)
