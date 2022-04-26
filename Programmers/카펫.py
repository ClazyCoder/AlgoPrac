# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

from itertools import combinations

def divisor(x):
    divisor_list = []
    for i in range(1,x+1):
        if x % i == 0:
            divisor_list.append(i)
    return divisor_list

def solution(brown, yellow):
    answer = []
    divisors = divisor(brown+yellow)
    for i in list(combinations(divisors,1)):
        i = i[0]
        j = (brown+yellow) // i
        if i > j: 
            temp = i
            i = j
            j = temp
        list1 = []
        for r in range(i):
            list2 = []
            for c in range(j):
                if r == 0 or r == i-1: list2.append(1)
                elif c == 0 or c == j-1: list2.append(1)
                else: list2.append(0)
            list1.append(list2)
        count_b = 0
        count_y = 0
        for l in list1:
            count_b += l.count(1)
            count_y += l.count(0)
        if count_b == brown and count_y == yellow: 
            answer.append(j) 
            answer.append(i)
            break
    return answer