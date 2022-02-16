import sys
for line in sys.stdin:
    iarr = line.split(' ')
    a = int(iarr[0])
    b = int(iarr[1])
    print(a+b)