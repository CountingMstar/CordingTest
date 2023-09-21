from collections import deque

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

q = deque()
frist = 1
q.append(frist)
visited[frist] = 1

while q:
    x = q.popleft()

    for i in graph[x]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1

print(sum(visited) - 1)





