import sys

input = sys.stdin.readline()
INF = int(1e9)

# g = [[1,2,2],[1,4,1],[1,3,5],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]
# n, m = 6, len(g)

g = [[1,2,6],[1,3,2],[2,4,2],[2,3,2],[3,5,1],[4,6,2],[5,2,-4],[5,4,3],[5,6,4]]
g = [[1,2,6],[1,3,2],[2,4,2],[2,3,2],[3,5,1],[4,6,2],[5,2,-2],[5,4,3],[5,6,4]]
n, m = 6, len(g)
start = 1

edges = []
dist = [INF] * (n+1)

for i in range(m):
    a, b, c = g[i][0], g[i][1], g[i][2]
    edges.append((a, b, c))


print(edges)


def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost

                if i == n-1:
                    return True

    return False


negative_cycle = bf(1)


if negative_cycle:
    print('-1')

else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])