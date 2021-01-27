def solve(s):
    word_list = s.split(' ')
    name_capitalized = []
    for word in word_list:
        name_capitalized.append(word.capitalize())
    word = ' '.join(name_capitalized)
    return word
