from collections import deque

N = int(input())
M = int(input())
INF = 1e9
relation = [sorted(list(map(int,input().split()))) for i in range(M)]

info = []
for i, j in relation:
    info.append(i)
    info.append(j)

info = list(sorted(set(info)))
graph = [[INF]*len(info) for i in range(len(info))]
for a in range(N):
    for b in range(N):
        if a == b:
            graph[a][b] = 0

for a, b in relation:
    graph[a-1][b-1] = 1

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

answer = 0
for i in graph[0]:
    if i < INF and i > 0:
        answer += 1

print(answer)
