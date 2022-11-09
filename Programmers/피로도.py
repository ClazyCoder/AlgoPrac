from itertools import permutations


def go(k, order, dungeons):
    done = 0
    for i in order:
        if k < dungeons[i][0]:
            break
        else:
            k -= dungeons[i][1]
            done += 1
    return done


def solution(k, dungeons):
    answer = 0
    l = list(range(len(dungeons)))
    order_list = list(permutations(l, len(l)))
    for order in order_list:
        d = go(k, order, dungeons)
        if d == len(dungeons):
            answer = d
            break
        elif d > answer:
            answer = d
    return answer
