import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드갯수 n, 간선갯수 m
n, m = 4, 3
# 시작노드 start 
start = 2

# 각 노드의 연결상태와 거리 
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
# print(graph)
# print(distance)

# 노드2에서 노드3으로 가는데 1만큼의 비용이 발생
g = [[2,1,1],[2,3,1],[3,4,1]]
for i in range(m):
    a, b, c = g[i]
    graph[a].append((b, c))

print(graph)

# n, m = map(int, input().split())
# start = int(input())

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# graph = [[2,1,1],[2,3,1],[3,4,1]]
# distance = [INF] * (len(graph))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        print('33333333333')
        print(q)
        dist, now = heapq.heappop(q)

        # 현재값이 이전값보다 크면(비효율적이면) 업로드하지 않음
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            print('4444444')
            print(i)
            cost = dist + i[1]
            
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)


for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])