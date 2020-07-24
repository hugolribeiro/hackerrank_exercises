# Programmer: Hugo Leça Ribeiro
# Date: 07/24/2020


def countingValleys(n, s):
    sea_level = 0
    valleys = 0
    for step in s:
        if step == 'U':
            sea_level += 1
            if sea_level == 0:
                valleys += 1
        elif step == 'D':
            sea_level -= 1
    return valleys
