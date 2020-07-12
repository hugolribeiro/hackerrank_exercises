# Complete the compareTriplets function below.
def compareTriplets(a, b):
    comparing = [0, 0]
    for index in range(0, 3):
        if a[index] > b[index]:
            comparing[0] += 1
        elif a[index] < b[index]:
            comparing[1] += 1
    return comparing

##################################
# a = list(map(int, input().rstrip().split()))
#
# b = list(map(int, input().rstrip().split()))
#
# result = compareTriplets(a, b)

