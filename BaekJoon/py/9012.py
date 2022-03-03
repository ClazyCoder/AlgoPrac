import sys

line = sys.stdin.readline()
N = int(line)
for i in range(N):
    count = 0
    words = sys.stdin.readline()
    for w in words:
        if w == '(':
            count += 1
        elif w == ')':
            count -= 1
        if count < 0:
            break
    if count == 0:
        print('YES')
    else:
        print('NO')