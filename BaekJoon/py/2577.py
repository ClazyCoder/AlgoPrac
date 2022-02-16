import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

s = str(a*b*c)
nList = [0,0,0,0,0,0,0,0,0,0]

for num in s:
    nList[int(num)] += 1
for i in nList:
    print(i)