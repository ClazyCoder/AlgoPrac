# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    keypad = {
        2 : [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4],
        5 : [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3],
        8 : [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2],
        0 : [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1]
    }
    left, right = 10, 11
    answer = ''
    for number in numbers:
        if number in [1,4,7]:
            left = number
            answer += 'L'
        elif number in [3,6,9]:
            right = number
            answer += 'R'
        else:
            if keypad[number][left] < keypad[number][right]:
                left = number
                answer += 'L'
            elif keypad[number][left] > keypad[number][right]:
                right = number
                answer += 'R'
            else:
                if hand == 'left':
                    left = number
                    answer += 'L'
                else:
                    right = number
                    answer += 'R'
    return answer