import sys

line = sys.stdin.readline()

iarr = line.split(' ')
a = int(iarr[0])
b = int(iarr[1])

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print("==")