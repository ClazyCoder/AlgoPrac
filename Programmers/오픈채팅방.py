# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

def solution(record):
    names = {}
    logs = []
    answer = []
    for str in record:
        str_list = str.split(' ')
        if(str_list[0] == "Enter"):
            names.update({str_list[1] : str_list[2]})
            logs.append((str_list[1], '님이 들어왔습니다.'))
        elif(str_list[0] == "Leave"):
            logs.append((str_list[1], '님이 나갔습니다.'))
        elif(str_list[0] == "Change"):
            names.update({str_list[1] : str_list[2]})
    for log in logs:
        answer.append(names[log[0]]+log[1])
    return answer