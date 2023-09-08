from collections import deque
import sys
import time

time1 = time.time()

input = sys.stdin.readline

N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
graph = [[0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[1,1,1,0,1,0,1],[0,0,0,0,1,1,1],
         [0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,0,0,0]]

def bfs(a,b):
    q = deque()
    total_count = 0
    q.append([a,b])
    graph[a][b] = 0

    while q:
        a,b = q.popleft()
        #  상
        if a-1 >= 0:
            if graph[a-1][b] == 1:
                q.append([a-1,b])
                graph[a-1][b] = 0
        #  하
        if a+1 <= N-1:
            if graph[a+1][b] == 1:
                q.append([a+1,b])
                graph[a+1][b] = 0
        #  좌
        if b-1 >= 0:
            if graph[a][b-1] == 1:
                q.append([a,b-1])
                graph[a][b-1] = 0
        #  우
        if b+1 <= N-1:
            if graph[a][b+1] == 1:
                q.append([a,b+1])
                graph[a][b+1] = 0

        total_count += 1

    return total_count

result = []
for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            total_count = bfs(a,b)
        # if total_count == 1:
            result.append(total_count)

print(len(result))
for r in result:
    print(r)

time2 = time.time()
print(time2-time1)


