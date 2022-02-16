import sys

nList = []
n = int(sys.stdin.readline())
for i in sys.stdin.readline().split(' '):
    nList.append(int(i))
average = 0.0
for i in nList:
    average += (i/max(nList))*100

print(average/n)