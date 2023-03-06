# https://school.programmers.co.kr/learn/courses/30/lessons/131705?language=python3

from itertools import *

def solution(number):
    count = 0
    """
    Permutations 순열
    Combinations 조합
    """
    printList = list(combinations(number, 3))
    for i in printList:
        if sum(i) == 0:
            count += 1
    return count


number = [-2, 3, 0, 2, -5]
answer = solution(number)
print(answer)
