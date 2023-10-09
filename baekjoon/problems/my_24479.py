from collections import deque
import sys
sys.setrecursionlimit(int(1e9))

input = sys.stdin.readline

N, M, R = map(int, input().split())
relation = [list(map(int, input().split())) for i in range(M)]
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)

for a, b in relation:
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

C = [0] * (N+1) 
def DFS(graph, R, visited, count, C):
    count += 1
    visited[R] = 1
    C[R] = count

    for i in graph[R]:
        if visited[i] == 0:
            DFS(graph, i, visited, count, C)

DFS(graph, R, visited, 0, C)

for i in range(1, len(C)):
    print(C[i])










