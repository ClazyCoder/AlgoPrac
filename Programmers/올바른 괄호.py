'''
def solution(s):
    answer = True
    num = 0
    for c in s:
        if c == '(':
            num += 1
        else:
            num -= 1
        if num == -1:
            return False
    if num == 0:
        answer = True
    else:
        answer = False

    return answer
'''

def solution(s):
    answer = True
    stack = []
    for c in s:
        if c == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            stack.append(c)
    if len(stack) == 0:
        answer = True
    else:
        answer = False

    return answer
