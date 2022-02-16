import sys

icase = sys.stdin.readline()
for num in range(int(icase)):
    line = sys.stdin.readline()
    iarr = line.split(',')
    a = int(iarr[0])
    b = int(iarr[1])
    print(a+b)