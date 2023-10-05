from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
visited = [0]*(100001)

def bfs(start):
    q = deque()
    n = 0
    q.append([start, n])

    while q:
        k, n = q.popleft()
        
        if k == K:
            print(n)
            break
        
        next = [[k+1,n+1],[k-1,n+1],[2*k,n+1]]
        for i in range(3):
            if 0 <= next[i][0] <= 100001 and visited[next[i][0]] == 0:
                q.append(next[i])

bfs(N)