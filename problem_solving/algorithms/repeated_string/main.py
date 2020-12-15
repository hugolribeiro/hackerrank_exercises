def repeatedString(s, n):
    length = len(s)
    times_repeat_word = n // length
    last_word = n % length
    amount_a = s.count('a') * times_repeat_word + (s[0:last_word].count('a'))
    return amount_a
