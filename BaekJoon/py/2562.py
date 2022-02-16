import sys

max_num = (0,1)

for i in range(9):
    num = int(sys.stdin.readline())
    if num > max_num[0]:
        max_num = (num,i+1)

print(max_num[0])
print(max_num[1])