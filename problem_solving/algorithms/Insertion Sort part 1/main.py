# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    element = arr[-1]
    sorted = False
    index_to_compair = n-2
    while not sorted:
        if element > arr[index_to_compair]:
            arr[index_to_compair+1] = element
            sorted = True
        else:
            arr[index_to_compair+1] = arr[index_to_compair]
            index_to_compair -= 1
            if index_to_compair == -2:
                arr[0] = element
                sorted = True
        for number in arr:
            print(number, end=' ')
        print()
