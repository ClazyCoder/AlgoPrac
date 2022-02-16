import sys

line = sys.stdin.readline()
x = int(line.split(' ')[1])
line = sys.stdin.readline().rstrip('\n').split(' ')

for istr in line:
    if int(istr) < x:
        print(istr,end=' ')