def equalizeArray(arr):
    unique_numbers = set(arr)
    max_times = 0
    for number in unique_numbers:
        if arr.count(number) > max_times:
            max_times = arr.count(number)
    remove_times = len(arr) - max_times
    return(remove_times)
