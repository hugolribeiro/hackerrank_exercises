def twoStrings(s1, s2):
    if set(s1).intersection(set(s2)) or set(s2).intersection(set(s1)):
        return 'YES'
    return 'NO'
