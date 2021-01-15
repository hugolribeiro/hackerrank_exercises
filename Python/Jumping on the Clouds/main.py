  # Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    minimum_jumps = 0
    length_c = len(c)
    cloud = 0
    while cloud < (length_c - 3):
        if c[cloud+2] == 0:
            minimum_jumps += 1
            cloud += 2
        else:
            minimum_jumps += 1
            cloud += 1
    minimum_jumps += 1
    return minimum_jumps
