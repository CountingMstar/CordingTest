from collections import deque
import sys
import time

input = sys.stdin.readline

N, M = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# graph = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]
# graph = [[1,1,0,1,1,0],[1,1,0,1,1,0],[1,1,1,1,1,1],[1,1,1,1,0,1]]
graph = [[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1],[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1]]
# graph = [[1,0,1,1,1,1,1],[1,1,1,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]

t1 = time.time()
check = [[0]*M for i in range(N)]

def bfs(graph,x,y,check):
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q.append([x,y])

    while True:
        if len(q) == 0:
            break

        x,y = q.popleft()
        ch = check[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx,ny])

                if check[nx][ny] > 0 and check[nx][ny] != ch + 1:
                    check[nx][ny] = min(check[nx][ny], ch + 1)
                elif check[nx][ny] == 0 and check[nx][ny] != ch + 1:
                    check[nx][ny] += ch + 1
    
    return check[-1][-1]+1


print(bfs(graph,0,0,check))
t2 = time.time()
print(t2-t1)

