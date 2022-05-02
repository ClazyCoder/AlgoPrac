# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    pokes = set(nums)
    answer = min(len(nums)//2, len(pokes))
    return answer