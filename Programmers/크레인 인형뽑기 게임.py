# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        m = m-1
        for i in range(len(board[0])):
            if board[i][m] > 0:
                if not basket:
                    basket.append(board[i][m])
                    board[i][m] = 0
                elif basket[-1] == board[i][m]:
                    board[i][m] = 0
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[i][m])
                    board[i][m] = 0
                break
    return answer