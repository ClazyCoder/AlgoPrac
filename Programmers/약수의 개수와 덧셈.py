# https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3

def divisor_even(x):
    count = 0
    for i in range(1,x+1):
        if x % i == 0:
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisor_even(i):
            answer += i
        else:
            answer -= i
    return answer