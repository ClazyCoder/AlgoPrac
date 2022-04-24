# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations : list):
    answer = 0
    citations.sort()
    for i in range(0,max(citations)):
        new_list = [x for x in citations if x >= i]
        new_list2 = [x for x in citations if x <= i]
        if len(new_list) >= i and len(new_list2) <= i:
            answer = i
    return answer