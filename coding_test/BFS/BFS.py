from collections import deque

# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# print(graph)


graph = [[1,1,0],[0,1,0],[0,1,1]]
n = len(graph)
m = len(graph[0])
print(str(n) + 'x' + str(m))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    print('111111111')
    print(queue)

    while queue:
        print('222222222')
        print(queue)
        x, y = queue.popleft()
        print(queue)
        print(x)
        print(y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print('33333333')
            print(nx)
            print(ny)

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                print('5555555')
                continue

            if graph[nx][ny] == 0:
                print('6666666')
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                print('7777777')

    return graph[n - 1][m - 1]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
