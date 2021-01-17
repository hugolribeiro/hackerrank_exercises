#My solution, without imports.

def squares(a, b):
    initial_integer = round(a ** 0.5) + (a ** 0.5 > round(a ** 0.5))
    final_integer = round(b ** 0.5) + (b ** 0.5 >= round(b ** 0.5))
    amount_squares = final_integer - initial_integer
    return amount_squares

#And my solution with 1 line:

def squares(a, b):
    return (round(b ** 0.5) + (b ** 0.5 >= round(b ** 0.5))) - (round(a ** 0.5) + (a ** 0.5 > round(a ** 0.5)))
