# Programmer: Hugo Leça Ribeiro

def print_formatted(number):
    max_size: int = len(bin(number)[2:])
    for n in range(1, number + 1):
        decimal = str(n).rjust(max_size)
        octa = oct(n)[2:].rjust(max_size)
        hexadecimal = hex(n)[2:].rjust(max_size)
        binary = bin(n)[2:].rjust(max_size)
        print(decimal, octa, hexadecimal.upper(), binary, sep=' ', end='\n')
