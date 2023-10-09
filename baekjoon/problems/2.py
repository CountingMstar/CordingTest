from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
ckeck_graph = [[0]*n for i in range(n)]
rule = [list(map(int, input().split())) for i in range(m)]
move = [[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1]]

# 지구는 둥글게
def earth(x, y):
    if 0 > x or x > n-1:
        if 0 > x:
            x = n - (abs(x) % 5)
        elif x > n-1:
            x = (x+1) % 5

    if 0 > y or y > n-1:
        if 0 > y:
            y = n - (abs(y) % 5)
        elif y > n-1:
            y = y % 5
    return x, y

# 첫 영향제 위치
loc_energy = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
print(loc_energy)

for l in loc_energy:
    ckeck_graph[l[0]][l[1]] = 1
# print(ckeck_graph)

for r in range(len(rule)):
    # 영양제 이동
    direction = rule[r][0]-1
    distance = rule[r][1]

    dx, dy = 0, 0
    for i in range(distance):
        dx += move[direction][0]
        dy += move[direction][1]

    new_loc_energy = []
    print('==== first ====')
    print(loc_energy)
    print(graph)
    for l in loc_energy:
        nx = l[0] + dx
        ny = l[1] + dy
        print('1111111')
        print(l[0])
        print(l[1])
        print(dx)
        print(dy)
        print(nx)
        print(ny)
        nx, ny = earth(nx, ny)
        print('2222222')
        print(nx)
        print(ny)
        # 자라기
        graph[nx][ny] += 1
        ckeck_graph[l[0]][l[1]] = 0

        new_loc_energy.append([nx,ny])

    print(new_loc_energy)

    print('666666666')
    print(graph)


    # 대각선 수만큼 더 자라기
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]

    for l in new_loc_energy:
        count = 0
        for i in range(4):
            nx, ny = l[0] + dx[i], l[1] + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and graph[nx][ny] >= 1:
                count += 1
        x = l[0]
        y = l[1]
        print('$$$$$$$')
        print(x)
        print(y)
        print(count)
        graph[x][y] += count
        ckeck_graph[x][y] = 1

    print('7777777777')
    print(graph)
    print(ckeck_graph)

    new_ckeck_graph = [[0]*n for i in range(n)]
    loc_energy = []
    result = 0
    # 새로운 영양제2
    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 2 and ckeck_graph[x][y] == 0:
                graph[x][y] -= 2
                new_ckeck_graph[x][y] = 1
                loc_energy.append([x,y])

            result += graph[x][y]
    
    print(graph)
    print(new_ckeck_graph)
    print(result)






