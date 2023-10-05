from collections import deque
import sys

input = sys.stdin.readline
N,M,V = map(int, input().split())

graph = [[] for i in range(N+1)]
visit = [0]*(N+1)

G = []
for i in range(1, M+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    G.append(a)
    G.append(b)

for i in range(len(graph)):
    graph[i].sort()

G = list(set(G))

def bfs(start):
    result = []
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        if v not in result:
            result.append(v)
            if len(result) == len(G):
                break

        for i in graph[v]:
            q.append(i)
    return result

result = []
def dfs(start):
    result.append(start)
    visit[start] = 1

    for i in range(1, N+1):
        if visit[i] == 0 and i in graph[start]:
            dfs(i)
    return result

D = dfs(V)
B = bfs(V)

for i in D:
    print(i, end=" ") 
print()
for i in B:
    print(i, end=" ") 