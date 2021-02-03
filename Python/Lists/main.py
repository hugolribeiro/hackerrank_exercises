if __name__ == '__main__':
    N = int(input())
    list_ = []
    for commands in range(0, N):
        command = input().split()
        if len(command) == 1:
            if command[0] == 'print':
                print(list_)
            else:
                eval(f'list_.{command[0]}()')
        elif len(command) == 2:
            eval(f'list_.{command[0]}({command[1]})')
        elif len(command) == 3:
            eval(f'list_.{command[0]}({command[1]},{command[2]})')
            
