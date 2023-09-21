from collections import deque

N = int(input())
# M = [list(map(int,input().split())) for i in range(N)]
# graph = [list(map(int, input().split())) for _ in range(N)]
M = [list(map(int,input())) for i in range(N)]
# M = [[0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[1,1,1,0,1,0,1],[0,0,0,0,1,1,1],
#      [0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,0,0,0]]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    M[x][y] = 0
    count = 0

    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while True:
        if len(q) == 0:
            break

        x,y = q.popleft()
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1 or M[nx][ny] == 0:
                continue

            q.append([nx,ny])
            M[nx][ny] = 0

    return count

counts = []
for x in range(N):
    for y in range(N):
        if M[x][y] != 0:
            counts.append(bfs(x,y))

counts = sorted(counts)
print(len(counts))
for i in counts:
    print(i)