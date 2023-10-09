import sys
sys.setrecursionlimit(1e9)

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

c = 1

def dfs(graph, v, visited):
    global c
    visited[v] = c

    for i in graph[v]:
        if visited[i] == 0:
            c += 1
            dfs(graph, i, visited)

for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

dfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])

