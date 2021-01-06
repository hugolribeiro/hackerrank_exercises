def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # Its length is at least 6.
    # It contains at least one digit.
    # It contains at least one lowercase English character.
    # It contains at least one uppercase English character.
    # It contains at least one special character. The special characters are: !@#$%^&*()-+
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    miss = 0
    
    if any(character in numbers for character in password)==False:
        miss += 1
    if any(character in lower_case for character in password)==False:
        miss += 1
    if any(character in upper_case for character in password)==False:
        miss += 1
    if any(character in special_characters for character in password)==False:
        miss += 1
    return max(miss, 6-n)
