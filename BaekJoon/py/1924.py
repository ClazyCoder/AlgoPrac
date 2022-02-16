s = input()
a = int(s.split(' ')[0])
b = int(s.split(' ')[1])
c = 0
for i in range(a):
    if i == 1:
        c += 31
    elif i == 2:
        c += 28
    elif i == 3:
        c += 31
    elif i == 4:
        c += 30
    elif i == 5:
        c += 31
    elif i == 6:
        c += 30
    elif i == 7:
        c += 31
    elif i == 8:
        c += 31
    elif i == 9:
        c += 30
    elif i == 10:
        c += 31
    elif i == 11:
        c += 30
    elif i == 12:
        c += 31
c += b
c %= 7
        
if c == 1:
    print('MON')
elif c == 2:
    print('TUE')
elif c == 3:
    print('WED')
elif c == 4:
    print('THU')
elif c == 5:
    print('FRI')
elif c == 6:
    print('SAT')
elif c == 0:
    print('SUN')