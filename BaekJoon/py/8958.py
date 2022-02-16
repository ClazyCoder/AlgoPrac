import sys

n = int(sys.stdin.readline())

for i in range(n):
    strlist = sys.stdin.readline()
    score = 0
    num = 0
    for s in strlist:
        if s == 'O':
            num += 1
            score += num
        elif s == 'X':
            num = 0
    print(score)