a = int(input())
for i in range(a):
    for j in range(a-1-i):
        print(' ',end='')
    for j in range(2*i+1):
        if j % 2 == 0:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
