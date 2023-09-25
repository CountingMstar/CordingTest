from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())

def bfs(start):
    q = deque()
    n = 0
    q.append([start, n])

    while q:
        k, n = q.popleft()
        
        if k == K:
            print(n)
            break

        q.append([k+1,n+1])
        q.append([k-1,n+1])
        q.append([2*k,n+1])

bfs(N)
