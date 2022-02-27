import sys

lines = sys.stdin.readline().split(' ')
h, m = int(lines[0]), int(lines[1])
lines2 = sys.stdin.readline()
time = int(lines2)

m += time
if m >= 60:
    h += m // 60
    m %= 60
if h >= 24:
    h -= 24

print(h, m)