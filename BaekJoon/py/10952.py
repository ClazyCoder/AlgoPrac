import sys
for line in sys.stdin:
    iarr = line.split(' ')
    a = int(iarr[0])
    b = int(iarr[1])
    if a==0 and b == 0:
        break
    print(a+b)