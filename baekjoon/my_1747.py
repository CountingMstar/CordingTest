from collections import deque
import sys
import math

input = sys.stdin.readline

N = int(input())

def sosu(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def fel(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

while True:
    if sosu(N) and fel(N):
        print(N)
        break
    N += 1





