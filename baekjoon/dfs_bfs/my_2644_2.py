from collections import deque

N = int(input())
A, B = map(int, input().split())
M = int(input())
relation = [list(map(int, input().split())) for i in range(M)]

INF = 1e9
graph = [[INF]*(N+1) for i in range(N+1)]
# lengh = [INF for i in range(N+1)]
# check = [[0]*(N+1) for i in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0

for i in range(len(relation)):
    a = relation[i][0]
    b = relation[i][1]

    graph[a][b] = 1
    graph[b][a] = 1

print('111111111')
print(graph)
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
print('2222222222')
print(graph)
print(A)
print(B)

if graph[A][B] == INF:
    print(-1)
else:
    print(graph[A][B])



