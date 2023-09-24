n = int(input())
A, B = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
res = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)

dfs(A)

if res[B] > 0:
    print(res[B])
else:
    print(-1)