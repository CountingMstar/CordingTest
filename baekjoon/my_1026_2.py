from collections import deque
import sys
import itertools

N = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []
def dfs(depth, list, n):
    if len(list) == n:
        answer.append(list)

    for i in range(depth, len(a)):
        dfs(i+1,list+[a[i]],n)

dfs(0,[],5)

print(answer)


