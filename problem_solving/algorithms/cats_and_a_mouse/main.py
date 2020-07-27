# Programmer: Hugo Leça Ribeiro
# Date: 10/27/2020

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    difA_mouse = z - x
    difB_mouse = z - y
    if abs(difA_mouse) == abs(difB_mouse):
        return 'Mouse C'
    if abs(difA_mouse) < abs(difB_mouse):
        return 'Cat A'
    else:
        return 'Cat B'
