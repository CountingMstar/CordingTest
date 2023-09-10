from collections import deque
import sys
import copy
import time

input = sys.stdin.readline
N = int(input())
time1 = time.time()

graph, m1, m2 = [], [], []
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    m1.append(min(tmp))
    m2.append(max(tmp))

m1, m2 = min(m1), max(m2)

print(graph)
print(m1)
print(m2)

def bfs(graph,x,y,w,m):
    q = deque()
    q.append([x,y])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    count = 1

    while q:
        if len(q) == 0:
            break 

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue

            if graph[nx][ny] > w:
                graph[nx][ny] = m
                q.append([nx,ny])
                count += 1

    return count

final_count = []

for w in range(m1,m2+1):
    graph2 = copy.deepcopy(graph)
    tmp = []
    for x in range(N):
        for y in range(N):
            if graph2[x][y] > w:
                tmp.append(bfs(graph2,x,y,w,m1))

    if len(tmp) == 0:
        final_count.append(1)
    else:
        final_count.append(len(tmp))
    # final_count.append(len(tmp))
    # graph = copy.deepcopy(graph2)

print(max(final_count))
time2 = time.time()
print(time2 - time1)