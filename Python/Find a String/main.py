def count_substring(string, sub_string):
    times = 0
    length = len(sub_string)
    for letter in range(0, len(string)):
        if string[letter:letter+length] == sub_string:
            times += 1
    return times
