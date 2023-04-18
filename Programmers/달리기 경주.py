# https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3

def solution(players, callings):
    answer = []
    np = {}
    pn = {}
    for i, p in enumerate(players):
        np[i] = p
        pn[p] = i
    for call in callings:
        idx = pn[call]
        temp = np[idx-1]
        np[idx] = temp
        np[idx-1] = call
        pn[call] = idx-1
        pn[temp] = idx
    for i in range(len(players)):
        answer.append(np[i])
    return answer
