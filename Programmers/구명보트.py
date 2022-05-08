# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

from collections import deque

def solution(people: list, limit : int):
    answer = 0
    q = deque(sorted(people))
    weight = 0
    while q:
        weight = q.pop()
        if q and q[0] + weight <= limit:
            q.popleft()
        answer += 1
    return answer