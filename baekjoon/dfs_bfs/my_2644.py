from collections import deque

N = int(input())
A, B = map(int, input().split())
M = int(input())
relation = [list(map(int, input().split())) for i in range(M)]

INF = 1e9
graph = [[] for i in range(N+1)]
lengh = [INF for i in range(N+1)]
check = [[0]*(N+1) for i in range(N+1)]

for i in range(len(relation)):
    a = relation[i][0]
    b = relation[i][1]

    graph[a].append(b)
    graph[b].append(a)

# print(graph)
# print(N)
# print(a)
# print(b)
# print(M)
# print(relation)

def bfs(A, B):
    q = deque()
    q.append(A)
    lengh[A] = 0

    while q:
        x = q.popleft()
        for y in graph[x]:
            if check[x][y] == 0:
                check[x][y] = 1
                check[y][x] = 1
                if lengh[x] != INF:
                    lengh[y] = lengh[x]+1
                else:
                    lengh[y] = 1

            else:
                continue

            q.append(y)

    if lengh[B] == INF:
        print(-1)
    else:
        print(lengh[B])

bfs(A, B)
print('111111111')
print(A)
print(B)
print(lengh)

