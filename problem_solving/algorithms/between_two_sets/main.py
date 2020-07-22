import math


# import os
# import random
# import re
# import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# Programmer: Hugo Leça Ribeiro
# Date: 07/17/2020


def calc_lcm(a):
    numbers_a = a
    divisors = []
    divisor = 2
    while sum(numbers_a) != len(numbers_a):
        times = 0
        for index in range(0, len(numbers_a)):
            if numbers_a[index] % divisor == 0:
                numbers_a[index] = numbers_a[index] / divisor
                times = 1
        if times == 1:
            divisors.append(divisor)
        else:
            divisor = next_prime(divisor)
    calculating_lcm = 1
    for divisor in divisors:
        calculating_lcm *= divisor
    return calculating_lcm


def next_prime(previous_prime):
    found = False
    tries = 0
    while not found:
        tries += 1
        actual_number = previous_prime + tries
        found = check_prime(actual_number)
    return found


def check_prime(actual_number):
    root = int(actual_number ** 0.5)
    for count in range(root, 1, -1):
        if actual_number % count == 0:
            return False
    return actual_number


def calc_gcd(list_b):
    result = list_b[0]
    for index in range(1, len(list_b)):
        result = math.gcd(result, list_b[index])
    return result


def find_multiples(lcm_a, gcd_b):
    factor = 1
    number = lcm_a
    multiples = []
    while number <= gcd_b:
        multiples.append(number)
        factor += 1
        number = factor * lcm_a
    return multiples


def final_verification(gcd_b, multiples):
    amount = 0
    for multiple in multiples:
        if gcd_b % multiple == 0:
            amount += 1
    return amount


def getTotalX(a, b):
    lcm_a = calc_lcm(a)
    gcd_b = calc_gcd(b)
    multiples = find_multiples(lcm_a, gcd_b)
    return final_verification(gcd_b, multiples)


#################################################
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     first_multiple_input = input().rstrip().split()
#
#     n = int(first_multiple_input[0])
#
#     m = int(first_multiple_input[1])
#
#     arr = list(map(int, input().rstrip().split()))
#
#     brr = list(map(int, input().rstrip().split()))
#
#     total = getTotalX(arr, brr)
#
#     fptr.write(str(total) + '\n')
#
#     fptr.close()
