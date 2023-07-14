# n, m = map(int, input().split())
# print(n)
# print(m)

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
# print(graph)

# graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
graph = [[0,0,0],[0,1,0],[1,0,1]]
n = len(graph)
m = len(graph[0])
print(str(n) + 'x' + str(m))


def dfs(x, y, num):
    print(num)
    num += 1
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1, y, num)
        dfs(x, y-1, num)
        dfs(x+1, y, num)
        dfs(x, y+1, num )

        return True
    return False

num = 0
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j, num) == True:
            print('##############')
            result += 1
        else:
            print('===========')
        

print(result)