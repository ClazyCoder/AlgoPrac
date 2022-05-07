# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
from itertools import combinations

def solution(numbers : list):
    answer = []
    ans_set = set()
    for i in list(combinations(numbers, 2)):
        ans_set.add(i[0] + i[1])
    answer = list(ans_set)
    answer.sort()
    return answer