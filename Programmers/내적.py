# https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3

def solution(a : list, b : list):
    answer = 0
    for i, j in zip(a, b):
        answer += i*j
    return answer