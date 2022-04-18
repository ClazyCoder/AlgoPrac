# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

def solution(prices : list):
    answer = [0] * len(prices)
    price_list = []
    price_list.append((prices.pop(0),0))
    i = 1
    for price in prices:
        if price >= price_list[-1][0]:
            for j in price_list:
                answer[j[1]] += 1
        else:
            for j in price_list:
                answer[j[1]] += 1
            p = price_list.pop()
            while price < p[0]:
                if price_list == []:
                    break
                p = price_list.pop()
            if price >= p[0]:
                price_list.append(p)
        price_list.append((price,i))
        i+=1   
    return answer