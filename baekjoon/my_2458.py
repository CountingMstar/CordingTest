from collections import deque
import sys

# N, M = 6, 6
# input = [[1,5],[3,4],[5,4],[4,2],[4,6],[5,2]]

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[0]*(N+1) for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

final_count = 0
for a in range(1, N+1):
    count = 0
    for b in range(1, N+1):
        count += graph[a][b] + graph[b][a]
    if count == N-1:
        final_count += 1

print(final_count)

