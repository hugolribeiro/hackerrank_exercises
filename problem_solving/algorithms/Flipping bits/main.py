def flippingBits(n):
    thirty_digits = "0" * 32
    thirty_digits = list(thirty_digits)
    print(thirty_digits)

    binary_number = (bin(n)[2:])

    for index in range(1, len(binary_number) + 1):
        thirty_digits[-index] = binary_number[-index]

    for index in range(0, 32):
        if (thirty_digits[index]) == '0':
            thirty_digits[index] = '1'
        else:
            thirty_digits[index] = '0'

    binary = ''.join(thirty_digits)
    return int(binary, 2)
