import sys

lines = sys.stdin.readline().split(' ')
numbers = []
for line in lines:
    numbers.append(int(line))
if numbers[0] == numbers[1] and numbers[0] == numbers[2]:
    print(10000 + numbers[0]*1000)
elif numbers[0] == numbers[1] or numbers[0] == numbers[2]:
    print(1000 + numbers[0]*100)
elif numbers[1] == numbers[2]:
    print(1000 + numbers[2]*100)
else:
    print(max(numbers)*100)