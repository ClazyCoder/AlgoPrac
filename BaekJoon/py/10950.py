import sys

line = sys.stdin.readline()
count = int(line)
for i in range(count):
    lines = sys.stdin.readline().split(' ')
    a = int(lines[0])
    b = int(lines[1])
    print(a+b)
