def saveThePrisoner(n, m, s):
    if m > n:
        rest = m % n
        if rest == 0 and s == 1:
            final_chair = n
        else:
            final_chair = s + (rest - 1)
    else:
        final_chair = (m + s) - 1
    if final_chair > n:
        final_chair = final_chair - n
    return final_chair
