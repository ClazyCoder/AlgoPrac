# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N, stages):
    answer = []
    percent_list = []
    for i in range(1, N+1):
        users = [x for x in stages if x >= i]
        if len(users) == 0:
            percent_list.append((i,0))
        else:
            fail_percent = stages.count(i) / len(users)
            percent_list.append((i,fail_percent))
    percent_list.sort(key = lambda x: x[1], reverse=True)
    for stage in percent_list:
        answer.append(stage[0])
    return answer