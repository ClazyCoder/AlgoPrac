# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
from itertools import permutations

def isPrime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def solution(numbers : str):
    answer = 0
    numberSet = set()
    for i in range(1,len(numbers)+1):
        numberList = list(permutations(numbers,i))
        for num in numberList:
            x = int(''.join(num))
            if isPrime(x):
                numberSet.add(x)
    answer = len(numberSet)
    return answer