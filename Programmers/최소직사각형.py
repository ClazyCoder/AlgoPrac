# https://programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):
    answer = 0
    list1 = []
    list2 = []
    for a, b in sizes:
        if a > b:
            list1.append(a)
            list2.append(b)
        else:
            list1.append(b)
            list2.append(a)
    answer = max(list1) * max(list2)
    return answer