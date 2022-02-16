import sys

nList = []
for i in range(10):
    num = int(sys.stdin.readline())
    if not num % 42 in nList:
        nList.append(num % 42)
print(len(nList))