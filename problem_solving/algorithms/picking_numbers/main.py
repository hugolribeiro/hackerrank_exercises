# Programmer: Hugo Leça Ribeiro
# Date: 29/07/2020

def pickingNumbers(a):
    numbers_tested = []
    amount_numbers = 1
    total = 0
    for index in range(0, len(a)-1):
        if a[index] not in numbers_tested:
            numbers_tested.append(a[index])
            amount_this_number = a.count(a[index])
            amountplus1 = a.count(a[index] + 1) + amount_this_number
            amountminus1 = a.count(a[index] - 1) + amount_this_number
            if amountplus1 >= total:
                total = amountplus1
            if amountminus1 >= total:
                total = amountminus1
            if total > amount_numbers:
                amount_numbers = total
        else:
            continue
    return(amount_numbers)
