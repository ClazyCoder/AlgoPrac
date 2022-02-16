import sys
line = sys.stdin.readline()
iarr = line.split(' ')
hour = int(iarr[0])
minute = int(iarr[1])
if hour == 0:
    hour = 24
time = hour * 60 + minute - 45
result_h = time // 60
if result_h == 24:
    result_h = 0
result_m = time % 60
print(result_h, result_m)