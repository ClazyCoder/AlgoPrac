import sys

average = 0
for i in range(5):
    line = sys.stdin.readline()
    num = int(line)
    if num < 40: num = 40
    average += num
print(int(average/5))