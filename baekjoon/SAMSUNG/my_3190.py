from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for i in range(K)]
L = int(input())
direction = [list(map(str, input().split())) for i in range(L)]

# 방향전환 타이밍
d_t = []
# 방향전환 방향
d_d = []
for i in direction:
    d_t.append(int(i[0]))
    d_d.append(i[1])

DD = [0, 1, 2, 3]
# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph = [[0]*N for i in range(N)]
for i in apple:
    x, y = i[0], i[1]
    graph[x-1][y-1] = 1

# print(graph)

D = 1
x, y = 0, 0
lengh = 1
q = deque()
APPLE = False
graph[x][y] = 2
second = 0
q.append([x, y])
while True:
    if second in d_t:
        strD = d_d[d_t.index(second)]
        # print('111111111')
        # print(D)
        # print(strD)
        if strD == 'D':
            D = (D+1) % 4
        if strD == 'L':
            D = (D+3) % 4

    if 0 <= x + dx[D] <= N-1 and 0 <= y + dy[D] <= N-1 and graph[x + dx[D]][y + dy[D]] != 2:
        nx = x + dx[D]
        ny = y + dy[D]   
        graph[nx][ny] = 2
        q.append([nx, ny])

        if APPLE == False:
            t = q.popleft()
            tx, ty = t[0], t[1]
            graph[tx][ty] = 0

        if APPLE == True:
            APPLE = False

        if graph[x + dx[D]][y + dy[D]] == 1:
            APPLE = True
            lengh += 1

        x, y = nx, ny

    elif 0 > x + dx[D] or  x + dx[D] >= N or 0 > y + dy[D] or y + dy[D] >= N or graph[x + dx[D]][y + dy[D]] == 2:
        second += 1
        break
    second += 1

print(second)



