import sys

input = sys.stdin.readline()
INF = int(1e9)

g = [[1,2,2],[1,4,1],[1,3,5],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]
n, m = 6, len(g)

graph = [[INF]*(n+1) for i in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b, c = g[i][0], g[i][1], g[i][2]
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):

        if graph[a][b] == INF:
            print('INF', end=' ')

        else:
            print(str(graph[a][b]), end=' ')
    print()
        
