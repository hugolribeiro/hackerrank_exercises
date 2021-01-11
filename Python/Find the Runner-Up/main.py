if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = max(arr)
    highest = max_score
    while highest == max_score:
        arr.remove(max_score)
        highest = max(arr)
    print(highest)
