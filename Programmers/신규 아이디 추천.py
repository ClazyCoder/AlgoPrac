# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

import re

def solution(new_id : str):
    answer = ''
    tempStr = new_id.lower()
    tempStr = re.sub(r"[^a-z-_.0-9]",'',tempStr)
    while tempStr.find('..') != -1:
        tempStr = tempStr.replace('..','.')
    tempStr = tempStr.strip('.')
    if tempStr == '': tempStr += 'a'
    tempStr = tempStr[:15]
    tempStr = tempStr.strip('.')
    while len(tempStr) < 3: tempStr += tempStr[-1]
    answer = tempStr
    return answer