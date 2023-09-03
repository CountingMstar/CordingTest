import heapq
import sys


input = sys.stdin.readline
INF = int(1e9)  # 무한

# n: 노드의 개수, m: 간선의 개수
# n, m = map(int, input().split())
# start = int(input())

g = [[1,2,2],[1,4,1],[1,3,5],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]
n, m = 6, len(g)
start = 1

# [a,b,c]
# a노드에서 b노드로 가는데, 비용 c가 듦
graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)


for i in range(m):
    a, b, c = g[i]
    graph[a].append((b, c))

print(graph)

def dijkstra(start):
    q = []
    # 리스트 q에 (0, start)를 우선순위 큐로 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue    # 바로 다음 사이클로 넘어감

        print('00000000000')
        print(dist)
        print(now)
        print(graph[now])

        for i in graph[now]:
            print('11111111111')
            print(i)
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
print(distance)


for i in range(1, n+1):
    
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])
    

