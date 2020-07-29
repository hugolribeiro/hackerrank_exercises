# Programmer: Hugo Leça Ribeiro
# Date: 29/07/2020

def pickingNumbers(a):
    amount_numbers = 1
    total = 0
    unique_numbers = set(a)
    for number in unique_numbers:
        times_this_number = a.count(number)
        plus1 = a.count(number + 1) + times_this_number
        minus1 = a.count(number - 1) + times_this_number
        if plus1 >= total:
            total = plus1
        if minus1 >= total:
            total = minus1
        if total > amount_numbers:
            amount_numbers = total
    return amount_numbers
