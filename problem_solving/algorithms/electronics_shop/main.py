# Programmer: Hugo Leça Ribeiro
# Date: 10/27/2020


def getMoneySpent(keyboards, drives, b):
    max_value = -1
    for keyboard in keyboards:
        for drive in drives:
            if max_value < (keyboard + drive) < b:
                max_value = keyboard + drive
    return max_value
