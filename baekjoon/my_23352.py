from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

print(N)
print(M)
print(graph)

def bfs(graph,x,y):
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count = 1
    q.append([x,y,count])
    start = graph[x][y]
    result = []
    
    while q:
        if len(q) == 0:
            break

        x,y,count = q.popleft()
        check = 0
        print('000000000')
        print([x,y])
        tmp = [x,y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 or graph[nx][ny] == 0 :
                check += 1
                continue

            if graph[nx][ny] != 0:
                graph[nx][ny] = 0
                count += 1
                q.append([nx,ny,count])

        if check == 4:
            end = graph[tmp[0]][tmp[1]]
            print('1111111111')
            print([start,end,count])
            result.append([start,end,count])

    print(result)

    # for i in range(len(result)):


# for x in range(N):
#     for y in range(M):

x = 4
y = 0
bfs(graph,x,y)
