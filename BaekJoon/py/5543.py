import sys

pay = 0
minimal = 2001
num = 0
for i in range(3):
    line = sys.stdin.readline()
    num = int(line)
    if minimal > num:
        minimal = num
pay += minimal
minimal = 2001
for i in range(2):
    line = sys.stdin.readline()
    num = int(line)
    if minimal > num:
        minimal = num
pay += minimal
print(pay-50)