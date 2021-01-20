def swap_case(s):
    new_word = ''
    for letter in s:
        if letter.islower():
            new_word += letter.upper()
        else:
            new_word += letter.lower()
    return new_word

# OR in one line:

def swap_case(s):
    return s.swapcase()
