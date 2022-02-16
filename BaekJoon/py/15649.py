import sys

def f(L, C, string):
    TL = L.copy()
    if C == 0:
        print(string)
        return
    for i in range(len(TL)):
        value = TL.pop(i)
        newstring = string + str(value) + ' '
        f(TL,C-1, newstring)
        TL.insert(i,value)

line = sys.stdin.readline()
N, M = line.split(' ')
N, M = int(N), int(M)
arr = list(range(1,N+1))
f(arr, M, '')