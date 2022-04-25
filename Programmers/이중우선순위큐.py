# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

import heapq

def solution(operations):
    answer = []
    heap = []
    for str in operations:
        if str[0] == 'I':
            parsed_str = str.split(' ')
            heapq.heappush(heap, int(parsed_str[1]))
        elif str[0] == 'D':
            parsed_str = str.split(' ')
            if not heap:
                pass
            elif parsed_str[1] == '1':
                heap.pop()
                heapq.heapify(heap)
            elif parsed_str[1] == '-1':
                heap.pop(0)
                heapq.heapify(heap)
    if not heap:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max(heap))
        answer.append(min(heap))
    return answer