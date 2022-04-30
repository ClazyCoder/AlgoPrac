# https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3

def solution(n):
    answer = 0
    new_number = []
    while n != 0:
        new_number.append(n % 3)
        n = n // 3
    for i, num in enumerate(new_number[::-1]):
        answer += num * 3**i
    return answer