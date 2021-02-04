def printError(e):
    print("Error Code: {}".format(e))

n = int(input())
for _ in range(n):
    try:
        a, b = map(int,input().split())
        print (a//b)
    except ValueError as e:
        printError(e)
    except ZeroDivisionError as e:
        printError(e)
        
#tries = int(input())
#for division in range(0, tries):
#    values = input().split(' ')
#    try:
#        a = int(values[0])
#        b = int(values[1])
#        print(a // b)
#    except ZeroDivisionError as zero_error:
#        print(f'Error Code: {zero_error}')
#    except ValueError as value_error:
#        print(f'Error code: {value_error}')       
