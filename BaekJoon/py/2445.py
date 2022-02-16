a = int(input())
for i in range(a-1):
    for j in range(i+1):
        print('*',end='')
    for j in range((a-1)*2-2*i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print('')
for i in range(2*a):
    print('*',end='')
print('')
for i in range(a-1):
    for j in range(a-i-1):
        print('*',end='')
    for j in range(2*(i+1)):
        print(' ',end='')
    for j in range(a-i-1):
        print('*',end='')
    print('')