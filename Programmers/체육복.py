# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):
    answer = 0
    set1 = set(lost)
    set2 = set(reserve)
    set3 = set1 & set2
    set1 -= set3
    set2 -= set3
    for i in set2:
        if (i-1) in set1:
            set1.remove(i-1)
        elif (i+1) in set1:
            set1.remove(i+1)
    answer = n - len(set1)
    return answer