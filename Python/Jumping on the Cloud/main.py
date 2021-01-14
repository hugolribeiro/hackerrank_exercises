# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    length = len(c)
    total_energy = 100
    actual_cloud = k
    if actual_cloud == length:
        actual_cloud = 0
    while actual_cloud != 0:
        if c[actual_cloud] == 1:
            total_energy -= 3
        else:
            total_energy -= 1
        actual_cloud = actual_cloud + k
        if actual_cloud >= length:
            actual_cloud = actual_cloud % length
    if c[0] == 0:
        total_energy -= 1
    else:
        total_energy -=3
    return total_energy      
