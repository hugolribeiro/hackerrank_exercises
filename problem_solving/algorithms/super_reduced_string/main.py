def super_reduced_string(string):
    new_string = list(string)
    i = 0
    length = len(new_string)
    while length > 1 and i < length-1:
        if new_string[i] == new_string[i+1]:
            del(new_string[i])
            del(new_string[i])
            i = 0
            length = len(new_string)
            continue
        i += 1
        length = len(new_string)
    if not new_string:
        return 'Empty String'
    return ''.join(new_string)
