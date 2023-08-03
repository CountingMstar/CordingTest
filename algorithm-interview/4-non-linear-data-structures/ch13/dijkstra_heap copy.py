import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())
n, m = 5, 8
start, end = 1, 5

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
past = [0] * (n+1)
print(past)
print(distance)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

g = [[1,2,2],[1,3,3],[1,4,1],[1,5,10],[2,4,2],[3,4,1],[3,5,1],[4,5,3]]
for i in range(m):
    a, b, c = g[i]
    graph[a].append((b, c))

print(graph)

def dijkstra(start, end):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, next_dist in graph[now]:
            cost = dist + next_dist

            if cost < distance[next]:
                distance[next] = cost
                past[next] = now
                heapq.heappush(q, (cost, next))

dijkstra(start, end)

ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = past[tmp]

ans.append(str(start))
ans.reverse()

print(distance[end])
print(len(ans))
print(" ".join(ans))

