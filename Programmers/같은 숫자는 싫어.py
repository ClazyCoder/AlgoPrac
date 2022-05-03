# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr : list):
    answer = []
    before = -1
    for i in arr:
        if before != i:
            answer.append(i)
            before = i
    return answer