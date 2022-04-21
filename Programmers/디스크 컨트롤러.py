# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

import heapq

def solution(jobs):
    answer = 0
    time_passed = 0
    jobs = sorted(jobs)
    working = []
    ready = []
    count = len(jobs)
    work = jobs.pop(0)
    working.append([work[1],work[0]])
    while working or ready:
        if working:
            done = working.pop()
            answer += done[0] + max(0, time_passed - done[1])
            time_passed = done[0] + max(time_passed, done[1])
        if jobs:
            job = jobs[0]
            while job[0] <= time_passed:
                heapq.heappush(ready, [job[1],job[0]])
                jobs.pop(0)
                if not jobs:
                    break
                job = jobs[0]
            heapq.heapify(ready)
            if not ready and jobs:
                job = jobs.pop(0)
                heapq.heappush(ready, [job[1],job[0]])
        if ready:
            work = heapq.heappop(ready)
            working.append(work)
    answer = int(answer/count)
    return answer