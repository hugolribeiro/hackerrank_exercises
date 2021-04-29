def twoStrings(s1, s2):
    if set(s1).intersection(set(s2)):
        return 'YES'
    return 'NO'
