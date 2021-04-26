# Programmer: Hugo Leça Ribeiro
# Date: 25/04/2021
# Complete the rotLeft function below.


def rotLeft(a, d):
    rotations = d % len(a)
    new_array = a.copy()
    for item in range(0, len(a)):
        new_array[item - rotations] = a[item]
    return new_array
