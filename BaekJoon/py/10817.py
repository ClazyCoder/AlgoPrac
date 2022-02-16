import sys

iarr = sys.stdin.readline().split(' ')
num1 = int(iarr[0])
num2 = int(iarr[1])
num3 = int(iarr[2])

if num1 > num2:
    if num1 < num3:
        print(num1)
    elif num2 > num3:
        print(num2)
    else:
        print(num3)
elif num1 < num2:
    if num2 < num3:
        print(num2)
    elif num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 < num3:
        print(num2)
    elif num1 > num3:
        print(num1)
    else:
        print(num3)