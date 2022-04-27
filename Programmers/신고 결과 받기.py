# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3

def solution(id_list : list, report : list, k : int):
    answer = [0] * len(id_list)
    report_list = []
    for i in range(len(id_list)):
        temp = []
        report_list.append(temp)
    report_count = [0] * len(id_list)
    for report_data in report:
        parsed_data = report_data.split(' ')
        user_index = id_list.index(parsed_data[0])
        reported_index = id_list.index(parsed_data[1])
        if report_list[user_index].count(reported_index) == 0:
            report_list[user_index].append(reported_index)
            report_count[reported_index] += 1
    for i, reported in enumerate(report_count):
        if reported >= k:
            for j, reporter in enumerate(report_list):
                if reporter.count(i) > 0:
                    answer[j] += 1
    return answer