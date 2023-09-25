from collections import deque
import sys
import copy

input = sys.stdin.readline
M, N, H = map(int, input().split())
INF = 1e9

graph = []
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)

distance = []
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append([INF]*M)
    distance.append(tmp)

def dfs(h, n, m):
    tmp_graph = copy.deepcopy(graph)
    tmp_distance = copy.deepcopy(distance)
    tmp_distance[h][n][m] = 0
    distance[h][n][m] = 0
    q = deque()
    q.append([h,n,m])

    while q:
        h,n,m = q.popleft()
        dh = [0,0,0,0,1,-1]
        dn = [-1,1,0,0,0,0]
        dm = [0,0,-1,1,0,0]

        for i in range(6):
            nh = h + dh[i]
            nn = n + dn[i]
            nm = m + dm[i]

            if nh<0 or nn<0 or nm<0 or nh>H-1 or nn>N-1 or nm>M-1 or tmp_graph[nh][nn][nm] == -1 or tmp_graph[nh][nn][nm] == 1:
                continue
            elif tmp_graph[nh][nn][nm] == 0:
                tmp_graph[nh][nn][nm] = 1
                tmp_distance[nh][nn][nm] = min(tmp_distance[nh][nn][nm], tmp_distance[h][n][m] + 1)
                distance[nh][nn][nm] = min(distance[nh][nn][nm], tmp_distance[nh][nn][nm])
                q.append([nh,nn,nm])
 

for k in range(H):
    for a in range(N):
        for b in range(M):
            if graph[k][a][b] == 1:
                dfs(k, a, b)


result = []
R = 0
for k in range(H):
    for a in range(N):
        for b in range(M):
            if graph[k][a][b] != -1:
                if distance[k][a][b] != INF:
                    result.append(distance[k][a][b])
                else:
                    R = -1

if R != 0:
    print(R)
else: 
    print(max(result))
