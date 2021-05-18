def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    length = len(arr)
    min_diff = 10 ** 10
    for number in range(1, length):
        pair_diff = abs(arr[number - 1] - arr[number])
        if pair_diff < min_diff:
            min_diff = pair_diff
    return min_diff
