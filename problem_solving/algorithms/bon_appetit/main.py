# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill

# Complete the bonAppetit function below.


def bonAppetit(bill, k, b):
    ana_amount = (sum(bill) - bill[k]) // 2
    if b == ana_amount:
        print('Bon Appetit')
    else:
        difference = b - ana_amount
        print(difference)
