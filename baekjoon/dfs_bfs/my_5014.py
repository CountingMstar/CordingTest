from collections import deque
import sys

input = sys.stdin.readline
F,S,G,U,D = map(int, input().split())
visited = [0] * (F+1)

def bfs(S):
    q = deque()
    n = 0
    q.append([S,n])
    visited[S] = 1

    while q:
        S, n = q.popleft()

        if S == G:
            return n
        
        if 1 <= S+U <= F:
            if visited[S+U] == 0:
                q.append([S+U,n+1])
                visited[S+U] = 1

        if 1 <= S-D <= F:
            if visited[S-D] == 0:
                q.append([S-D,n+1])
                visited[S-D] = 1

    return 'use the stairs'

print(bfs(S))
