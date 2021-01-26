def wrap(string, max_width):
    result = ''
    for letter in range(0, len(string), max_width):
        result += string[letter:letter+max_width]
        result += '\n'
    return result
