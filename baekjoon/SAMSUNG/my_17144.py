from collections import deque
import sys, copy

input = sys.stdin.readline
R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for t in range(T):

    tmp_graph = [[0]*C for i in range(R)]
    aircon = []

    # 미세먼지 확산
    for r in range(R):
        for c in range(C):
            if graph[r][c] == -1:
                tmp_graph[r][c] = -1
                aircon.append([r, c])
            ###########
            # else:
            #     tmp_graph[r][c] = graph[r][c]
            ###########

            if graph[r][c] > 0:
                check = []
                for i in range(4):
                    if 0 <= r + dx[i] <= R-1 and 0 <= c + dy[i] <= C-1 and graph[r + dx[i]][c + dy[i]] > -1:
                        check.append(i)
                
                n = len(check)
                if n > 0:
                    score = int(graph[r][c] / 5)
                    self_score = graph[r][c] - score*n

                    for i in check:
                        nx = r + dx[i]
                        ny = c + dy[i]
                        tmp_graph[nx][ny] += score

                    tmp_graph[r][c] += self_score

    # 미세먼지 회전
    r, c = aircon[0][0], aircon[0][1]
    for nr in range(r-1):
        tmp_graph[r-nr-1][0] = tmp_graph[r-nr-2][0]
    for nc in range(C-1):
        tmp_graph[0][nc] = tmp_graph[0][nc+1]
    for nr in range(r):
        tmp_graph[nr][-1] = tmp_graph[nr+1][-1]
    for nc in range(C-1):
        if nc == C-2:
            tmp_graph[r][C-1-nc] = 0
        else:
            tmp_graph[r][C-1-nc] = tmp_graph[r][C-1-nc-1]


    r, c = aircon[1][0], aircon[1][1]
    for nr in range(R-1-r-1):
        tmp_graph[r+nr+1][0] = tmp_graph[r+nr+2][0]
    for nc in range(C-1):
        tmp_graph[-1][nc] = tmp_graph[-1][nc+1]
    for nr in range(R-1-r):
        tmp_graph[R-1-nr][-1] = tmp_graph[R-1-nr-1][-1]
    for nc in range(C-1):
        if nc == C-2:
            tmp_graph[r][C-1-nc] = 0
        else:
            tmp_graph[r][C-1-nc] = tmp_graph[r][C-1-nc-1]

    # graph = tmp_graph
    graph = copy.deepcopy(tmp_graph)

total_score = 0
for i in graph:
    total_score += sum(i)
total_score += 2
print(total_score)



