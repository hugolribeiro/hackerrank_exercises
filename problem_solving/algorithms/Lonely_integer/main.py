def lonelyinteger(a):
    setA = set(a)
    for number in setA:
        if a.count(number) == 1:
            return number

a = [1, 1, 2, 3, 3]

print(lonelyinteger(a))