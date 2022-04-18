# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

import queue

def solution(bridge_length : int, weight : int, truck_weights : list):
    answer = 0
    on_bridge_weight = 0
    on_bridge_count = 0
    bridge = queue.Queue()
    exit_time = []
    while truck_weights != [] or not bridge.empty():
        answer += 1
        if exit_time == []:
            pass
        elif answer == exit_time[0]:
            on_bridge_weight -= bridge.get()
            on_bridge_count -=1
            exit_time.pop(0)
        if truck_weights == []:
            pass
        elif on_bridge_weight + truck_weights[0] <= weight and on_bridge_count < bridge_length:
            truck = truck_weights.pop(0)
            bridge.put(truck)
            exit_time.append(answer+bridge_length)
            on_bridge_weight += truck
            on_bridge_count += 1
    return answer