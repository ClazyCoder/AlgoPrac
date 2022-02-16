a = int(input())
for i in range(a):
    for j in range(a-1-i):
        print(' ',end='')
    for j in range(2*i+1):
        if i == a-1:
            print('*',end='')
        elif j == 0 or j==2*i:
            print('*',end='')
        else:
            print(' ',end='')
    print('')