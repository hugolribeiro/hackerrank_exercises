cube = lambda x: pow(x, 3) 

def fibonacci(n):
    sequence = [0, 1]
    for index in range(2, n):
        sequence.append(sequence[index-2] + sequence[index-1])
    return sequence[0:n]

    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
