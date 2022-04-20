from functools import cmp_to_key

def sort(x, y):
    a = int(str(x)+str(y))
    b = int(str(y)+str(x))
    return b - a

def solution(numbers):
    answer = ''
    res = sorted(numbers, key=cmp_to_key(sort))
    for i in res:
        answer += ''.join(str(i))
    if answer[0] == '0' : answer = '0'
    return answer