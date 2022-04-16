# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    ansDict = {
        6 : 1,
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        0 : 6
    }
    answer = []
    a = set(lottos)
    b = set(win_nums)
    least = len(a & b)
    zeros = lottos.count(0)
    best = least + zeros
    if best <=1 : best = 0
    if least <=1 : least = 0
    answer.append(ansDict[best])
    answer.append(ansDict[least])
    return answer