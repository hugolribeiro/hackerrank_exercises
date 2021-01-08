def missingNumbers(arr, brr):
    difference = []
    unique_numbers = set(brr)
    for number in unique_numbers:
        times_in_brr = brr.count(number)
        times_in_arr = arr.count(number)
        if times_in_brr != times_in_arr:
            difference.append(number)
    return difference
