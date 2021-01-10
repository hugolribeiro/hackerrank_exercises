if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # Without comprehension
    # lista = []
    # for x1 in range(0, x+1):
    #     for y1 in range(0, y+1):
    #         for z1 in range(0, z+1):
    #             if x1+y1+z1 != 3:
    #                 lista.append([x1, y1, z1])
    # print(lista)
    
    # With comprehension
    comprehension = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n]
    print(comprehension)
