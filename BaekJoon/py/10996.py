import sys

n = int(sys.stdin.readline())
if n == 1:
    print('*')
elif n % 2 == 0:
    for i in range(n):
        for j in range(n//2):
            print('* ',end='')
        print('')
        for k in range(n//2):
            print(' *',end='')
        print('')
else:
    for i in range(n):
        for j in range(n//2+1):
            print('* ',end='')
        print('')
        for k in range(n//2):
            print(' *',end='')
        print('')
