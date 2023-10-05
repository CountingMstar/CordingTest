from collections import deque
import sys, copy

input = sys.stdin.readline
N = int(input())

graph = []
relations = []
for i in range(N**2):
    if i < N:
        graph.append([0]*N)
    relations.append(list(map(int, input().split())))

tmp_graph = copy.deepcopy(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check_relation(me, rel, graph):

    tmp = []
    max_like, max_empty = 0, 0
    for x in range(N):
        for y in range(N):
            like, empty = 0, 0
            if graph[x][y] == 0:

                for i in range(4):
                    if 0 <= x + dx[i] <= N-1 and 0 <= y + dy[i] <= N-1:

                            nx = x + dx[i]
                            ny = y + dy[i]

                            # 좋아하는 학생이 인접 근처에 몇명인지?
                            if graph[nx][ny] in rel:
                                like += 1

                            # 인접 근처에 빈자리가 몇개인지?
                            if graph[nx][ny] == 0:
                                empty += 1

                if max_like <= like:
                    max_like = like
                    tmp.append([x,y,like,empty])
    
    # 좋아하는 사람수가 제일 큰 개체 고르기
    tmp2 = []
    for i in tmp:
        x, y, like, empty = i[0], i[1], i[2], i[3]
        if like == max_like:
            tmp2.append(i)
            if max_empty <= empty:
                max_empty = empty
    if len(tmp2) == 1:
        x, y, like, empty = tmp2[0][0], tmp2[0][1], tmp2[0][2], tmp2[0][3]
        graph[x][y] = me
        return graph
    tmp = tmp2

    # 인접 빈칸이 많은 곳
    tmp2 = []
    min_x = 1e9
    for i in tmp:
        x, y, like, empty = i[0], i[1], i[2], i[3]
        if max_empty == empty:
            tmp2.append(i)
            if min_x >= x:
                min_x = x
    if len(tmp2) == 1:
        x, y, like, empty = tmp2[0][0], tmp2[0][1], tmp2[0][2], tmp2[0][3]
        graph[x][y] = me
        return graph
    tmp = tmp2

    # 행이 작은곳
    tmp2 = []
    min_y = 1e9
    for i in tmp:
        x, y, like, empty = i[0], i[1], i[2], i[3]
        if min_x == x:
            tmp2.append(i)
            if min_y >= y:
                min_y = y
    if len(tmp2) == 1:
        x, y, like, empty = tmp2[0][0], tmp2[0][1], tmp2[0][2], tmp2[0][3]
        graph[x][y] = me
        return graph
    tmp = tmp2

    # 열이 작은곳
    tmp2 = []
    for i in tmp:
        x, y, like, empty = i[0], i[1], i[2], i[3]
        if min_y == y:
            tmp2.append(i)
    if len(tmp2) == 1:
        x, y, like, empty = tmp2[0][0], tmp2[0][1], tmp2[0][2], tmp2[0][3]
        graph[x][y] = me
        return graph
    
    else:
        print('========== Error ==========')


def score(graph):
    s = 0
    for x in range(N):
        for y in range(N):
            
            c = 0
            for i in range(4):
                if 0 <= x + dx[i] <= N-1 and 0 <= y + dy[i] <= N-1:
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if graph[nx][ny] in re[graph[x][y]]:
                        c += 1

            if c == 0:
                t = 0  
            if c == 1:
                t = 1  
            if c == 2:
                t = 10  
            if c == 3:
                t = 100
            if c == 4:
                t = 1000

            s += t

    return s  

re = {}
for r in relations:
    i = r[0]
    j = r[1:]
    re[i] = j

    graph = check_relation(i,j,graph)

print(score(graph))


