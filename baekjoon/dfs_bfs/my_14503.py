from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
Map = [list(map(int, input().split())) for i in range(N)]

Map[r][c] = 2

def robot(r,c,d):
    # 북동남서
    A = [[r-1,c],[r,c+1],[r+1,c],[r,c-1]]
    info = [[] for i in range(4)]

    # 0:청소x, 1:벽, 2:청소O
    for k, i in enumerate(A):
        r, c = i[0], i[1]
        if 0 <= r < N and 0 <= c < M:
            if Map[r][c] == 1:
                info[k].append(1)
            elif Map[r][c] == 0:
                info[k].append(0)
            elif Map[r][c] == 2:
                info[k].append(2)
        else:
            info[k].append(1)

    if A[d] == 0:
        r


            

