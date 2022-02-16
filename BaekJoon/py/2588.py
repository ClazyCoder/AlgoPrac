import sys

a = sys.stdin.readline().rstrip('\n')
b = sys.stdin.readline().rstrip('\n')

for value in range(len(b)):
    print(int(a)*int(b[len(b)-value-1]))
print(int(a)*int(b))