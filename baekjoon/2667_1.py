from collections import deque
import sys
import time

time1 = time.time()

input = sys.stdin.readline

N = int(input())
# graph = [list(map(int, input())) for _ in range(N)]
graph = [[0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[1,1,1,0,1,0,1],[0,0,0,0,1,1,1],
         [0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,0,0,0]]

def bfs(graph,x,y):

    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append((x,y))
    
    graph[x][y] = 0
    cnt = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1

    return cnt


count = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count.append(bfs(graph,i,j))
print(count)
count.sort()
print(count)
print(len(count))

for i in range(len(count)):
    print(count[i])

time2 = time.time()
print(time2-time1)