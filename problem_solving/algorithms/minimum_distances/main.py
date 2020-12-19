def minimumDistances(a):
    min_distance = -1
    length = len(a)
    for number in range(0, length-1):
        for another_number in range(number+1, length):
            if a[number] == a[another_number]:
                distance = another_number - number
                if min_distance == -1:
                    min_distance = distance
                elif min_distance > distance:
                    min_distance = distance
    return min_distance
