def solution(distance, scope, times):
    answer = 0
    for i in scope:
        i.sort()
    guards = list(zip(scope, times))
    guards.sort(key=lambda x: x[0][0])
    for walk in range(1, distance+1):
        for guard in guards:
            if walk >= guard[0][0] and walk <= guard[0][1] and (
                    walk % (guard[1][0] + guard[1][1])) <= guard[1][0] and walk % (guard[1][0] + guard[1][1]) > 0:
                answer = walk
                return answer
        answer = walk
    return answer
