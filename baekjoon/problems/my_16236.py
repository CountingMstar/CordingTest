from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for i in range(N)]
size = 2

tmp = []
for a in range(N):
    for b in range(N):
        if graph[a][b] == 9:
            fish_loc = [a, b]
        if 0 < graph[a][b] < size:
            tmp.append([a, b])

print(tmp)
print(fish_loc)

def bfs(x,y):
    q = deque()
    q.append(x,y)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            if 0 <= x + dx[i] <= N-1 and 0 <= y + dy[i] <= N-1 and graph[x + dx[i]][y + dy[i]] <= size:
                nx = x + dx[i]
                ny = y + dy[i] 
