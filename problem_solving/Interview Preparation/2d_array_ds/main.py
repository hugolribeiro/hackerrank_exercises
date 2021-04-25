# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses_sum = []
    for line in range(1, 5):
        for column in range(1, 5):
            hourglass_sum = arr[line-1][column-1] + arr[line-1][column] + arr[line-1][column+1] + arr[line][column] + arr[line+1][column-1] + arr[line+1][column] + arr[line+1][column+1]
            hourglasses_sum.append(hourglass_sum)
    return max(hourglasses_sum)
