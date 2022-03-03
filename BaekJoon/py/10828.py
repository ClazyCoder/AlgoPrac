from sys import stdin

line = stdin.readline()
N = int(line)
stack = []
for i in range(N):
    command = stdin.readline().strip()
    if command.split(' ')[0] == 'push':
        stack.append(int(command.split(' ')[1]))
    elif command.split(' ')[0] == 'top':
        if stack == []:
            print('-1')
        else:
            print(stack[-1])
    elif command.split(' ')[0] == 'size':
        print(len(stack))
    elif command.split(' ')[0] == 'empty':
        if stack == []:
            print('1')
        else:
            print('0')
    elif command.split(' ')[0] == 'pop':
        if stack == []:
            print('-1')
        else:
            print(stack.pop())