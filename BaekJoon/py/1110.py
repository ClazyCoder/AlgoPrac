import sys

line = sys.stdin.readline()
start_num = int(line)
num = start_num
cycle = 0
last_num = -1
while start_num != last_num:
    cycle += 1
    new_num = num//10 + num%10
    last_num = (num%10)*10+(new_num%10)
    num = last_num
print(cycle)