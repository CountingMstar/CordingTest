from collections import deque
import sys

short_men = [int(input()) for i in range(9)]
seven_short_men = []

def dfs(depth, start):
    if depth == 7:
        if sum(seven_short_men) == 100:
            for j in sorted(seven_short_men):
                print(j)
            exit()

        else:
            return 
    
    for i in range(start, len(short_men)):
        seven_short_men.append(short_men[i])
        dfs(depth+1, i+1)
        seven_short_men.pop()

dfs(0, 0)


